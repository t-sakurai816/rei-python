import requests

URL = "https://raw.githubusercontent.com/IUI-Lab/MATRICS-Corpus/master/utterance/BP-S1.txt"


def main():
    data = get_url_data()
    # print(data)
    return 0


# URLからデータを取得する
def get_url_data():
    result = requests.get(URL)
    data = result.text
    return data


if __name__ == "__main__":
    main()
