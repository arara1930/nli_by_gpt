import json
import re
from collections import Counter


def read_json(path: str):
    # ファイルを開いてJSONデータを読み込む
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def pic_up_deepcase(sentence: str) -> list:
    # 正規表現パターン: <と>で囲まれた内容を抽出
    pattern = r"<(.*?)>"  # 非貪欲マッチで <> に囲まれた文字列を取得
    # 抽出
    matches = re.findall(pattern, sentence)

    return matches


def are_arrays_equal(arr1, arr2):
    # 要素と出現回数を比較
    return Counter(arr1) == Counter(arr2)


def count_and_print_deep_case_consistency_num(target_path: str) -> None:
    datas = read_json(path=target_path)

    # define_key
    key_id = 'sentence_pair_id'
    key_s1 = 'sentence_1'
    key_s2 = 'sentence_2'

    deep_consistency_ids = []
    deep_un_consistency_ids = []
    for record in datas:
        s1_deep_list = pic_up_deepcase(sentence=record[key_s1])
        s2_deep_list = pic_up_deepcase(sentence=record[key_s2])

        if are_arrays_equal(arr1=s1_deep_list, arr2=s2_deep_list):
            deep_consistency_ids.append(record[key_id])
        else:
            deep_un_consistency_ids.append(record[key_id])

    print(target_path)
    print('完全一致', len(deep_consistency_ids))
    print('非一致', len(deep_un_consistency_ids))


def main():
    target_directory = '../logAndResult/gpt-4o-mini/ver2/part1/analysis/'
    target_path = target_directory+'withdeep_only_true.json'
    count_and_print_deep_case_consistency_num(target_path=target_path)

    target_path = target_directory+'nodeep_only_true.json'
    count_and_print_deep_case_consistency_num(target_path=target_path)

    target_path = target_directory+'both_true.json'
    count_and_print_deep_case_consistency_num(target_path=target_path)

    target_path = target_directory+'both_false.json'
    count_and_print_deep_case_consistency_num(target_path=target_path)


if __name__ == "__main__":
    main()
