import yaml
import json


def read_jsonFile(config_path: str):
    # jsonの場合
    # 設定ファイルを読み込み
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    # outputファイルのパスを設定
    output_path = config["openai"]["log_folder"] + \
        config["openai"]["output"]

    # result_outputファイルのパスを設定
    result_output_path = config["openai"]["log_folder"] + \
        config["calc"]["result_file"]

    # ファイルを開いてJSONデータを読み込む
    with open(output_path, 'r', encoding='utf-8') as f:
        datas = json.load(f)

    # idと前提文と仮定文と正解ラベルのkeyを指定
    key_id = 'sentence_pair_id'
    key_s1 = 'sentence_1'
    key_s2 = 'sentence_2'
    key_true_label = 'true_label'
    key_pred_label = 'pred_label'

    return result_output_path, datas, key_id, key_s1, key_s2, key_true_label, key_pred_label
