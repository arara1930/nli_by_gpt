import yaml
import json
import check_json_or_jsonl


class ReadFile:
    def __init__(self, config_path: str) -> None:
        # 設定ファイルを読み込み
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        self.config = config

    def get_config(self):
        return self.config

    def read_jsonFile(self):
        config = self.get_config()
        json_or_jsonl_flag = check_json_or_jsonl.detect_file_format(
            config['openai']['input'])

        if json_or_jsonl_flag == 'JSON':
            # jsonの場合
            # inputファイルのパスを設定
            input_path = config["openai"]["input"]

            # ファイルを開いてJSONデータを読み込む
            with open(input_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # idと前提文と仮定文と正解ラベルのkeyを指定
            key_id = 'sentence_pair_id'
            key_s1 = 'sentence_1'
            key_s2 = 'sentence_2'
            key_true_label = 'label'

        elif json_or_jsonl_flag == 'JSONL':
            # jsonlの場合
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

        else:
            print("Invalid format")

        return data, key_id, key_s1, key_s2, key_true_label


# def read_configFile(config_path: str):
#     with open(config_path, "r") as file:
#         config = yaml.safe_load(file)
#     return config


# def read_jsonFile(config_path: str):
#     # 設定ファイルを読み込み
#     config = read_configFile(config_path=config_path)

#     json_or_jsonl_flag = check_json_or_jsonl.detect_file_format(
#         config['openai']['input'])

#     if json_or_jsonl_flag == 'JSON':
#         # jsonの場合
#         # inputファイルのパスを設定
#         input_path = config["openai"]["input"]

#         # ファイルを開いてJSONデータを読み込む
#         with open(input_path, 'r', encoding='utf-8') as f:
#             data = json.load(f)

#         # idと前提文と仮定文と正解ラベルのkeyを指定
#         key_id = 'sentence_pair_id'
#         key_s1 = 'sentence_1'
#         key_s2 = 'sentence_2'
#         key_true_label = 'label'

#     elif json_or_jsonl_flag == 'JSONL':
#         # jsonlの場合
#         # 設定ファイルを読み込み
#         with open(config_path, "r") as file:
#             config = yaml.safe_load(file)

#         # inputファイルのパスを設定
#         input_path = config["openai"]["input"]

#         # json形式を開く
#         with open(input_path, 'r', encoding='utf-8') as file:
#             data = [json.loads(l) for l in file.readlines()]

#         # idと前提文と仮定文と正解ラベルのkeyを指定
#         key_id = 'sentence_pair_id'
#         key_s1 = 'sentence1'
#         key_s2 = 'sentence2'
#         key_true_label = 'label'

#     else:
#         print("Invalid format")

#     return data, key_id, key_s1, key_s2, key_true_label

def main():
    config_path = '../logAndResult/gpt-4o/part1/withdeep/config.yaml'
    read_file = ReadFile(config_path=config_path)

    data, key_id, key_s1, key_s2, key_true_label = read_file.read_jsonFile()

    print(key_id, key_s1, key_s2, key_true_label)


if __name__ == "__main__":
    main()
