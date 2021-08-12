import requests
import json as JSON

URL = "https://raw.githubusercontent.com/IUI-Lab/MATRICS-Corpus/master/utterance/BP-S1.txt"


def main():
    data = get_url_data()
    # print(data)
    return 0


# URLからデータを取得する
def get_url_data():
    result = requests.get(URL)
    data = []
    json = {}
    # list de kakomanaito object ga detekuru
    lines = list(map(lambda x: x.split("\t"),result.text.splitlines()))

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
    #return JSON.dumps(data, ensure_ascii=False)

if __name__ == "__main__":
    main()
