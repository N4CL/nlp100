# encoding: utf-8

"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""


def sort(file_path):

    line_list = []
    with open(file_path, "r") as f:
        lines = f.readlines()

        # 各行を比較できるように、一行ごとにリスト化
        line_list += [line.split() for line in lines]

    # バブルソート
    while True:
        is_sort = False

        for i in xrange(len(line_list)-1):
            # 3カラム目で比較
            if float(line_list[i][2]) < float(line_list[i+1][2]):
                line_list[i], line_list[i+1] = line_list[i+1], line_list[i]
                is_sort = True

        if not is_sort:
            break

    # リスト化された行を再度元のtab区切りの形に戻す
    item = ["\t".join(items) for items in line_list]
    print "\n".join(item)


if __name__ == '__main__':
    sort("hightemp.txt")
