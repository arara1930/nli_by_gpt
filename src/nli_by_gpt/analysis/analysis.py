from nli_by_gpt.use_gpt_api.make_file_path import MakeFilePath
import json


class DefineFilePath:
    def __init__(self, config_path: str):
        self.make_file_path = MakeFilePath(config_path)

    def get_withdeep_only_true_path_for_analysis(self):
        # withdeep_only_true.jsonのパスを指定
        withdeep_only_true_path_for_analysis = self.make_file_path.make_withdeep_only_true_path_for_analysis()
        return withdeep_only_true_path_for_analysis

    def get_nodeep_only_true_path_for_analysis(self):
        # nodeep_only_true.jsonのパスを指定
        nodeep_only_true_path_for_analysis = self.make_file_path.make_nodeep_only_true_path_for_analysis()
        return nodeep_only_true_path_for_analysis

    def get_both_true_path_for_analysis(self):
        # both_true.jsonのパスを指定
        both_true_path_for_analysis = self.make_file_path.make_both_true_path_for_analysis()
        return both_true_path_for_analysis

    def get_both_false_path_for_analysis(self):
        # both_false.jsonのパスを指定
        both_false_path_for_analysis = self.make_file_path.make_both_false_path_for_analysis()
        return both_false_path_for_analysis


def make_json_file(file_path: str, data: list):
    # JSON形式の文字列に変換
    json_data = json.dumps(data, ensure_ascii=False, indent=4)

    # ファイルに書き出す
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json_data)


def main():
    config_path = '../logAndResult/gpt-4o/part1/withdeep/config.yaml'
    # make_file_pathを初期化
    make_file_path = MakeFilePath(config_path)
    # combined.jsonのパスを指定
    combined_json_path_for_analysis = make_file_path.make_combined_json_path_for_analysis()
    # both_true.jsonのパスを指定
    both_true_path_for_analysis = make_file_path.make_both_true_path_for_analysis()
    # both_false.jsonのパスを指定
    both_false_path_for_analysis = make_file_path.make_both_false_path_for_analysis()
    # withdeep_only_true.jsonのパスを指定
    withdeep_only_true_path_for_analysis = make_file_path.make_withdeep_only_true_path_for_analysis()
    # nodeep_only_true.jsonのパスを指定
    nodeep_only_true_path_for_analysis = make_file_path.make_nodeep_only_true_path_for_analysis()

    # ファイルを開いてJSONデータを読み込む
    with open(combined_json_path_for_analysis, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # idと前提文と仮定文と正解ラベルのkeyを指定
    key_id = 'sentence_pair_id'
    key_s1 = 'sentence_1'
    key_s2 = 'sentence_2'
    key_true_label = 'true_label'
    key_withdeep_pred_label = 'withdeep_pred'
    key_nodeep_pred_label = 'nodeep_pred'

    both_true = []
    both_false = []
    withdeep_only_true = []
    nodeep_only_true = []
    for record in data:
        withdeep_true = (record[key_true_label] ==
                         record[key_withdeep_pred_label])
        withdeep_false = (record[key_true_label] !=
                          record[key_withdeep_pred_label])
        nodeep_true = (record[key_true_label] == record[key_nodeep_pred_label])
        nodeep_false = (record[key_true_label] !=
                        record[key_nodeep_pred_label])

        # both_trueファイルの作成
        if withdeep_true and nodeep_true:
            both_true.append(record)

        # both_falseファイルの作成
        if withdeep_false and nodeep_false:
            both_false.append(record)

        # withdeep_only_trueファイルの作成
        if withdeep_true and nodeep_false:
            withdeep_only_true.append(record)

        # nodeep_only_trueファイルの作成
        if withdeep_false and nodeep_true:
            nodeep_only_true.append(record)

    print('number_of_both_true')
    print(len(both_true))
    print('number_of_both_false')
    print(len(both_false))
    print('number_of_withdeep_only_true')
    print(len(withdeep_only_true))
    print('number_of_nodeep_only_true')
    print(len(nodeep_only_true))

    # both_trueファイルの作成
    make_json_file(file_path=both_true_path_for_analysis, data=both_true)
    # both_falseファイルの作成
    make_json_file(file_path=both_false_path_for_analysis, data=both_false)
    # withdeep_only_trueファイルの作成
    make_json_file(file_path=withdeep_only_true_path_for_analysis,
                   data=withdeep_only_true)
    # nodeep_only_trueファイルの作成
    make_json_file(file_path=nodeep_only_true_path_for_analysis,
                   data=nodeep_only_true)


if __name__ == "__main__":
    main()
