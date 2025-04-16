import json
from nli_by_gpt.use_gpt_api.make_file_or_path import MakeFileOrPath
from nli_by_gpt.use_gpt_api.read_file import ReadFile


def combine(make_file_or_path: MakeFileOrPath, read_file: ReadFile):
    # output.jsonのパスを指定(analysis用、withdeep)
    outputFile_withdeep_path_for_analysis = make_file_or_path.make_outputFile_withdeep_path_for_analysis()
    # output.jsonのパスを指定(analysis用、nodeep)
    outputFile_nodeep_path_for_analysis = make_file_or_path.make_outputFile_nodeep_path_for_analysis()
    # combined.jsonのパスを指定
    combined_json_path_for_analysis = make_file_or_path.make_combined_json_path_for_analysis()

    # combined.jsonに必要なkeyの取得
    data_withdeep, key_id, key_s1, key_s2, key_true_label, key_pred_label, key_log = read_file.get_jsonFile_keys_for_analysis(
        outputFile_withdeep_path_for_analysis)
    data_nodeep, key_id, key_s1, key_s2, key_true_label, key_pred_label, key_log = read_file.get_jsonFile_keys_for_analysis(
        outputFile_nodeep_path_for_analysis)

    combined_dict_list = []
    for record_withdeep, record_nodeep in zip(data_withdeep, data_nodeep):
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


def combine_for_three_methods(make_file_or_path: MakeFileOrPath, read_file: ReadFile):
    # output.jsonのパスを指定(analysis用、withdeep)
    outputFile_withdeep_path_for_analysis = make_file_or_path.make_outputFile_withdeep_path_for_analysis()
    # output.jsonのパスを指定(analysis用、nodeep)
    outputFile_nodeep_path_for_analysis = make_file_or_path.make_outputFile_nodeep_path_for_analysis()
    # output.jsonのパスを指定(analysis用、ensembled)
    outputFile_ensembled_path_for_analysis = make_file_or_path.make_outputFile_ensembled_path_for_analysis()
    # combined.jsonのパスを指定
    combined_json_path_for_analysis = make_file_or_path.make_combined_for_three_methods_json_path_for_analysis()

    # combined.jsonに必要なjsonの取得
    data_withdeep = read_file.get_data(
        target_path=outputFile_withdeep_path_for_analysis
    )
    data_nodeep = read_file.get_data(
        target_path=outputFile_nodeep_path_for_analysis
    )
    data_ensembled = read_file.get_data(
        target_path=outputFile_ensembled_path_for_analysis
    )

    # keyの指定
    key_id = 'sentence_pair_id'
    key_s1 = 'sentence_1'
    key_s2 = 'sentence_2'
    key_true_label = 'true_label'
    key_pred = 'pred_label'
    key_ensembled_pred = 'key_ensembled_pred'

    combined_dict_list = []
    for record_withdeep, record_nodeep, record_ensembled in zip(data_withdeep, data_nodeep, data_ensembled):
        pred_pattern = []
        for pred_label in [record_withdeep[key_pred], record_nodeep[key_pred], record_ensembled[key_ensembled_pred]]:
            if pred_label == 'contradiction':
                pred_pattern.append('c')
            elif pred_label == 'entailment':
                pred_pattern.append('e')
            elif pred_label == 'neutral':
                pred_pattern.append('n')
            else:
                pred_pattern.append(' ')

        error_pattern = []
        for pred in pred_pattern:
            if record_withdeep[key_true_label] == 'contradiction':
                if pred == 'c':
                    error_pattern.append('t')
                elif pred == 'e' or pred == 'n':
                    error_pattern.append('f')
                else:
                    error_pattern.append(' ')
            if record_withdeep[key_true_label] == 'entailment':
                if pred == 'e':
                    error_pattern.append('t')
                elif pred == 'c' or pred == 'n':
                    error_pattern.append('f')
                else:
                    error_pattern.append(' ')
            if record_withdeep[key_true_label] == 'neutral':
                if pred == 'n':
                    error_pattern.append('t')
                elif pred == 'c' or pred == 'e':
                    error_pattern.append('f')
                else:
                    error_pattern.append(' ')

        result_record = {
            "sentence_pair_id": record_withdeep[key_id],
            "sentence_1": record_withdeep[key_s1],
            "sentence_2": record_withdeep[key_s2],
            "true_label": record_withdeep[key_true_label],
            "pred_pattern": pred_pattern,
            "error_pattern": error_pattern,
            "withdeep_pred": record_withdeep[key_pred],
            "nodeep_pred": record_nodeep[key_pred],
            "ensembled_pred": record_ensembled[key_ensembled_pred]
        }
        combined_dict_list.append(result_record)

    # JSON形式の文字列に変換
    json_data = json.dumps(combined_dict_list, ensure_ascii=False, indent=4)

    # ファイルに書き出す
    with open(combined_json_path_for_analysis, 'w', encoding='utf-8') as f:
        f.write(json_data)


def main():
    config_path = "../../logAndResult/part1/withdeep/config.yaml"
    # make_file_or_pathを初期化
    make_file_or_path = MakeFileOrPath(config_path)
    # read_fileを初期化
    read_file = ReadFile(config_path=config_path)

    combine(make_file_or_path=make_file_or_path, read_file=read_file)


if __name__ == "__main__":
    main()
