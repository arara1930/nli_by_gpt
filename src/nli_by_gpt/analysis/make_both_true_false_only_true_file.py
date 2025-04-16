from nli_by_gpt.use_gpt_api.read_file import ReadFile
from nli_by_gpt.use_gpt_api.make_file_or_path import MakeFileOrPath


def make_both_true_false_only_true_file(
        read_file: ReadFile,
        make_file_or_path: MakeFileOrPath,
        combined_json_path_for_analysis: str,
        both_true_path_for_analysis: str,
        both_false_path_for_analysis: str,
        withdeep_only_true_path_for_analysis: str,
        nodeep_only_true_path_for_analysis: str,
) -> list:
    # ファイルを開いてJSONデータを読み込む
    data = read_file.get_data(target_path=combined_json_path_for_analysis)

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

    # both_trueファイルの作成
    make_file_or_path.make_output_json_file(
        result_dicts=both_true,
        output_path=both_true_path_for_analysis
    )
    # both_falseファイルの作成
    make_file_or_path.make_output_json_file(
        result_dicts=both_false,
        output_path=both_false_path_for_analysis
    )
    # withdeep_only_trueファイルの作成
    make_file_or_path.make_output_json_file(
        result_dicts=withdeep_only_true,
        output_path=withdeep_only_true_path_for_analysis
    )
    # nodeep_only_trueファイルの作成
    make_file_or_path.make_output_json_file(
        result_dicts=nodeep_only_true,
        output_path=nodeep_only_true_path_for_analysis
    )

    print('number_of_both_true')
    print(len(both_true))
    print('number_of_both_false')
    print(len(both_false))
    print('number_of_withdeep_only_true')
    print(len(withdeep_only_true))
    print('number_of_nodeep_only_true')
    print(len(nodeep_only_true))

    # return用リストの作成
    list_for_append_result_txt = []
    list_for_append_result_txt.append('number_of_both_true')
    list_for_append_result_txt.append(len(both_true))
    list_for_append_result_txt.append('number_of_both_false')
    list_for_append_result_txt.append(len(both_false))
    list_for_append_result_txt.append('number_of_withdeep_only_true')
    list_for_append_result_txt.append(len(withdeep_only_true))
    list_for_append_result_txt.append('number_of_nodeep_only_true')
    list_for_append_result_txt.append(len(nodeep_only_true))

    return list_for_append_result_txt


def make_only_true_file_for_three_methods(
        read_file: ReadFile,
        make_file_or_path: MakeFileOrPath,
        combined_json_path_for_analysis: str,
        all_true_path_for_analysis: str,
        all_false_path_for_analysis: str,
        withdeep_only_true_path_for_analysis: str,
        withdeep_ensemble_true_path_for_analysis: str,
        nodeep_only_true_path_for_analysis: str,
        nodeep_ensemble_true_path_for_analysis: str,
):
    def make_record_with_error_pred_label(record: list, key_error_pred_label: str):
        record_with_error_pred_label = {
            'sentence_pair_id': record[key_id],
            'sentence_1': record[key_s1],
            'sentence_2': record[key_s2],
            'true_label': record[key_true_label],
            'pred_pattern': record[key_pred_pattern],
            'error_pattern': record[key_error_pattern],
            'error_pred_label': record[key_error_pred_label],
            'withdeep_pred': record[key_withdeep_pred_label],
            'nodeep_pred': record[key_nodeep_pred_label],
            'key_ensembled_pred': record[key_ensembled_pred],
        }
        return record_with_error_pred_label

    # ファイルを開いてJSONデータを読み込む
    data = read_file.get_data(target_path=combined_json_path_for_analysis)

    # idと前提文と仮定文と正解ラベルのkeyを指定
    key_id = 'sentence_pair_id'
    key_s1 = 'sentence_1'
    key_s2 = 'sentence_2'
    key_true_label = 'true_label'
    key_pred_pattern = 'pred_pattern'
    key_error_pattern = 'error_pattern'
    key_withdeep_pred_label = 'withdeep_pred'
    key_nodeep_pred_label = 'nodeep_pred'
    key_ensembled_pred = 'ensembled_pred'

    all_true = []
    all_false = []
    withdeep_only_true = []
    withdeep_ensemble_true = []
    nodeep_only_true = []
    nodeep_ensemble_true = []

    # 正誤パターンの振り分け
    for record in data:
        error_pattern_str = "".join(record[key_error_pattern]).strip()

        if error_pattern_str == 'ttt':
            record_with_error_pred_label = make_record_with_error_pred_label(
                record=record,
                key_error_pred_label=key_withdeep_pred_label
            )
            all_true.append(record_with_error_pred_label)
        elif error_pattern_str == 'fff':
            record_with_error_pred_label = make_record_with_error_pred_label(
                record=record,
                key_error_pred_label=key_withdeep_pred_label
            )
            all_false.append(record_with_error_pred_label)
        elif error_pattern_str == 'tff':
            record_with_error_pred_label = make_record_with_error_pred_label(
                record=record,
                key_error_pred_label=key_nodeep_pred_label
            )
            withdeep_only_true.append(record_with_error_pred_label)
        elif error_pattern_str == 'tft':
            record_with_error_pred_label = make_record_with_error_pred_label(
                record=record,
                key_error_pred_label=key_nodeep_pred_label
            )
            withdeep_ensemble_true.append(record_with_error_pred_label)
        elif error_pattern_str == 'ftf':
            record_with_error_pred_label = make_record_with_error_pred_label(
                record=record,
                key_error_pred_label=key_withdeep_pred_label
            )
            nodeep_only_true.append(record_with_error_pred_label)
        elif error_pattern_str == 'ftt':
            record_with_error_pred_label = make_record_with_error_pred_label(
                record=record,
                key_error_pred_label=key_withdeep_pred_label
            )
            nodeep_ensemble_true.append(record_with_error_pred_label)

    # all_trueファイルの作成
    make_file_or_path.make_output_json_file(
        result_dicts=all_true,
        output_path=all_true_path_for_analysis
    )
    # all_falseファイルの作成
    make_file_or_path.make_output_json_file(
        result_dicts=all_false,
        output_path=all_false_path_for_analysis
    )
    # withdeep_only_trueファイルの作成
    make_file_or_path.make_output_json_file(
        result_dicts=withdeep_only_true,
        output_path=withdeep_only_true_path_for_analysis
    )
    # withdeep_ensemble_trueファイルの作成
    make_file_or_path.make_output_json_file(
        result_dicts=withdeep_ensemble_true,
        output_path=withdeep_ensemble_true_path_for_analysis
    )
    # nodeep_only_trueファイルの作成
    make_file_or_path.make_output_json_file(
        result_dicts=nodeep_only_true,
        output_path=nodeep_only_true_path_for_analysis
    )
    # nodeep_ensemble_trueファイルの作成
    make_file_or_path.make_output_json_file(
        result_dicts=nodeep_ensemble_true,
        output_path=nodeep_ensemble_true_path_for_analysis
    )

    # # return用リストの作成
    # list_for_append_result_txt = []
    # list_for_append_result_txt.append('number_of_both_true')
    # list_for_append_result_txt.append(len(both_true))
    # list_for_append_result_txt.append('number_of_both_false')
    # list_for_append_result_txt.append(len(both_false))
    # list_for_append_result_txt.append('number_of_withdeep_only_true')
    # list_for_append_result_txt.append(len(withdeep_only_true))
    # list_for_append_result_txt.append('number_of_nodeep_only_true')
    # list_for_append_result_txt.append(len(nodeep_only_true))

    # return list_for_append_result_txt


def main():
    print()


if __name__ == "__main__":
    main()
