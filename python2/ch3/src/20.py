# encoding: utf-8

"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json


def extract_uk():
    with open("jawiki-country.json", "r") as f:
        json_data = f.readline()
        target = ""
        while json_data:
            load = json.loads(json_data)
            if load["title"] == u"イギリス":
                target = load["text"]
                break
            json_data = f.readline()
    return target


def main():
    text = extract_uk().encode("utf-8")

    # 記事本文の表示
    print text

    # jawiki-country.jsonが大きいので、利用する部分だけ書き出す
    with open("uk.txt", "w") as f:
        f.write(text)


if __name__ == '__main__':
    main()
