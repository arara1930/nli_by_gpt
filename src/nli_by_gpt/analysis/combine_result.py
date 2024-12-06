import json
from nli_by_gpt.use_gpt_api.make_file_path import MakeFilePath
from nli_by_gpt.use_gpt_api.read_file import ReadFile


def combine(config_path: str):
    # make_file_pathを初期化
    make_file_path = MakeFilePath(config_path)
    # output.jsonのパスを指定(analysis用、withdeep)
    outputFile_withdeep_path_for_analysis = make_file_path.make_outputFile_withdeep_path_for_analysis()
    # output.jsonのパスを指定(analysis用、nodeep)
    outputFile_nodeep_path_for_analysis = make_file_path.make_outputFile_nodeep_path_for_analysis()
    # combined.jsonのパスを指定
    combined_json_path_for_analysis = make_file_path.make_combined_json_path_for_analysis()

    # combined.jsonに必要なkeyの取得
    # read_fileを初期化
    read_file = ReadFile(config_path=config_path)
    data_withdeep, key_id, key_s1, key_s2, key_true_label, key_pred_label = read_file.get_jsonFile_keys_for_analysis(
        outputFile_withdeep_path_for_analysis)
    data_nodeep, key_id, key_s1, key_s2, key_true_label, key_pred_label = read_file.get_jsonFile_keys_for_analysis(
        outputFile_nodeep_path_for_analysis)

    combined_dict_list = []
    for record_withdeep, record_nodeep in zip(data_withdeep, data_nodeep):
        print(record_withdeep)
        print(key_true_label)
        result_record = {
            "sentence_pair_id": record_withdeep[key_id],
            "sentence_1": record_withdeep[key_s1],
            "sentence_2": record_withdeep[key_s2],
            "true_label": record_withdeep[key_true_label],
            "withdeep_pred": record_withdeep[key_pred_label],
            "nodeep_pred": record_nodeep[key_pred_label]
        }
        combined_dict_list.append(result_record)

    # JSON形式の文字列に変換
    json_data = json.dumps(combined_dict_list, ensure_ascii=False, indent=4)

    # ファイルに書き出す
    with open(combined_json_path_for_analysis, 'w', encoding='utf-8') as f:
        f.write(json_data)


def main():
    config_path = "../logAndResult/gpt-4o/part1/withdeep/config.yaml"

    combine(config_path=config_path)


if __name__ == "__main__":
    main()
