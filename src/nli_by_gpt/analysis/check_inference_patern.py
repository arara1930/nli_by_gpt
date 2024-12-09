from nli_by_gpt.analysis.analysis import DefineFilePath
import json


def check_inference_patern(config_path: str, target_data: str, true_label: str, pred_label):
    define_file_path = DefineFilePath(config_path=config_path)
    # target_file_path = define_file_path.get_withdeep_only_true_path_for_analysis()
    target_file_path = define_file_path.get_nodeep_only_true_path_for_analysis()

    # idと前提文と仮定文と正解ラベルのkeyを指定
    key_id = 'sentence_pair_id'
    key_s1 = 'sentence_1'
    key_s2 = 'sentence_2'
    key_true_label = 'true_label'
    key_withdeep_pred_label = 'withdeep_pred'
    key_nodeep_pred_label = 'nodeep_pred'

    if target_data == 'both_true' or target_data == 'both_false':
        if target_data == 'both_true':
            # both_true.jsonのパスを指定
            target_file_path = define_file_path.get_both_true_path_for_analysis()

        if target_data == 'both_false':
            # both_false.jsonのパスを指定
            target_file_path = define_file_path.get_both_false_path_for_analysis()

        # ファイルを開いてJSONデータを読み込む
        with open(target_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        num_of_target = 0
        target_record_ids = []
        for record in data:
            if record[key_true_label] == true_label:
                num_of_target += 1

    if target_data == 'with_deep_only_true':
        # pathの指定
        target_file_path = define_file_path.get_withdeep_only_true_path_for_analysis()

        # ファイルを開いてJSONデータを読み込む
        with open(target_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        num_of_target = 0
        target_record_ids = []
        for record in data:
            if (record[key_true_label] == true_label) and (record[key_nodeep_pred_label] == pred_label):
                num_of_target += 1
                target_record_ids.append(record[key_id])

    if target_data == 'no_deep_only_true':
        # pathの指定
        target_file_path = define_file_path.get_nodeep_only_true_path_for_analysis()

        # ファイルを開いてJSONデータを読み込む
        with open(target_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        num_of_target = 0
        target_record_ids = []
        for record in data:
            if (record[key_true_label] == true_label) and (record[key_withdeep_pred_label] == pred_label):
                num_of_target += 1
                target_record_ids.append(record[key_id])

    return num_of_target, target_record_ids


def main():
    config_path = '../logAndResult/gpt-4o/part1/withdeep/config.yaml'
    # target_data = 'with_deep_only_true'
    target_data = 'no_deep_only_true'
    # target_data = 'both_true'
    # target_data = 'both_false'

    # true_label = 'entailment'
    # true_label = 'neutral'
    true_label = 'contradiction'

    # pred_label = 'entailment'
    pred_label = 'neutral'
    # pred_label = 'contradiction'
    num_of_target, target_record_ids = check_inference_patern(
        config_path=config_path,
        target_data=target_data,
        true_label=true_label,
        pred_label=pred_label
    )
    print(num_of_target)
    print(target_record_ids)


if __name__ == "__main__":
    main()
