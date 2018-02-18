# coding: utf-8

"""
60. KVSの構築
Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．
"""

from redis import StrictRedis
from json import loads


def main():
    json_data = []
    with open("artist.json", 'r') as _file:
        for line in _file.readlines():
            # json stringをdic型に変換
            json_data.append(loads(line))

    r = StrictRedis(host='localhost', port=6379, db=0)

    # Redisに登録
    for dic in json_data:

        if "area" in dic:
            r.set(dic["name"], dic["area"])


if __name__ == '__main__':
    main()
