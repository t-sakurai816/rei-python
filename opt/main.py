import requests

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

if __name__ == "__main__":
    main()
