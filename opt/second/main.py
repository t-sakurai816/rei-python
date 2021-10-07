import json as JSON

FILE = 'BP-S1-A-0.txt'
WINDOW_SIZE = 30
KEY = " AU01_c"


def main():
    data = open_file(FILE)
    json = create_json(data)
    list_data = JSON.loads(json)
    del list_data[0]
    result = list()

    for i in range((int(len(list_data)/30))):
        if (i == 0):
            result.append(calc_ave(list_data, KEY, i, WINDOW_SIZE))
        else:
            result.append(calc_ave(list_data, KEY, i+3, WINDOW_SIZE + 3))

    for i in result:
        print(KEY, i)

    return 0


def open_file(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
    return data


def create_json(file_data):
    data = list()
    json = {}
    # convert from object to list
    lines = list(map(lambda x: x.split("\t"), file_data.splitlines()))

    # properties = ["timestamp", "AU01_c", "AU02_c", "AU04_c","AU05_c"]
    properties = lines[0]

    for line in lines:
        text = {}
        for index, item in enumerate(line):
            text[properties[index]] = item
        """
        {
            "timestamp": int,
            "AU01_c": int,
            "AU02_c": int,
            "AU04_c": int,
            "AU05_c": int
        }
        """
        data.append(text)

    for index, value in enumerate(data):
        json[index] = value

    # use data or json
    return JSON.dumps(data, ensure_ascii=False)


def calc_ave(list_data, key, start, end):
    count = 0
    num_list = list()
    for i in list_data[start: end]:
        # print(i[key])
        num_list.append(i[key])
        count += 1

    num_list_int = list(map(int, num_list))
    ave = sum(num_list_int) / len(num_list_int)
    return ave


if __name__ == "__main__":
    main()
