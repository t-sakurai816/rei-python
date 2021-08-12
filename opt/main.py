import requests
import json as JSON
import json
import statistics

URL = "https://raw.githubusercontent.com/IUI-Lab/MATRICS-Corpus/master/utterance/BP-S1.txt"


def main():
    json_data = create_json(get_url_data())
    list_data = json.loads(json_data)
    del list_data[0]  # delete first line
    print(calc_ave_of_start_end(list_data))
    return 0


# get data from URL
def get_url_data():
    result = requests.get(URL)
    data = result.text
    return data


# create json from dict_data
def create_json(dict_data):
    data = []
    json = {}
    # convert from object to list
    lines = list(map(lambda x: x.split("\t"), dict_data.splitlines()))

    # properties = ["ID", "start", "end", "transcription"]
    properties = lines[0]

    for line in lines:
        text = {}
        for index, item in enumerate(line):
            text[properties[index]] = item
        """
        {
            "ID": string,
            "start": string,
            "end": string,
            "transcription": string
        }
        """
        data.append(text)

    for index, value in enumerate(data):
        json[index] = value

    # use data or json
    return JSON.dumps(data, ensure_ascii=False)


# Calculate the average of start and end(-1)
def calc_ave_of_start_end(data):
    calc_result = []
    start_list = []
    end_list = []
    for i in data:
        start_list.append(float(i["start"]))
        end_list.append(float(i["end"]))
    for i in range(len(start_list)):
        calc_result.append(start_list[i+1] - end_list[i])
        if i == len(start_list) - 2:
            break
    # print(calc_result)
    ave = statistics.mean(calc_result)

    return ave


if __name__ == "__main__":
    main()
