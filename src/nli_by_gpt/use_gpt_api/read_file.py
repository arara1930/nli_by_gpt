import yaml
import json


def read_file(config_path: str):
    # # jsonの場合
    # # 設定ファイルを読み込み
    # with open(config_path, "r") as file:
    #     config = yaml.safe_load(file)

    # # inputファイルのパスを設定
    # input_path = config["openai"]["input"]

    # # ファイルを開いてJSONデータを読み込む
    # with open(input_path, 'r', encoding='utf-8') as f:
    #     data = json.load(f)

    # # idと前提文と仮定文と正解ラベルのkeyを指定
    # key_id = 'sentence_pair_id'
    # key_s1 = 'sentence_1'
    # key_s2 = 'sentence_2'
    # key_true_label = 'label'

    # jsonlの場合
    # 設定ファイルを読み込み
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    # inputファイルのパスを設定
    input_path = config["openai"]["input"]

    # json形式を開く
    with open(input_path, 'r', encoding='utf-8') as file:
        data = [json.loads(l) for l in file.readlines()]

    # idと前提文と仮定文と正解ラベルのkeyを指定
    key_id = 'sentence_pair_id'
    key_s1 = 'sentence1'
    key_s2 = 'sentence2'
    key_true_label = 'label'

    return data, key_id, key_s1, key_s2, key_true_label
