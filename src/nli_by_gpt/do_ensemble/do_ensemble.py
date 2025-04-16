from nli_by_gpt.use_gpt_api.make_file_or_path import MakeFileOrPath
from nli_by_gpt.use_gpt_api.read_file import ReadFile
from nli_by_gpt.analysis import check_deep_case_consistency
from nli_by_gpt.calc import calc_for_ensembled_json


def check_deep_case_exact_match(record: dict, key_s1: str, key_s2: str) -> str:
    s1_deep_list = check_deep_case_consistency.pic_up_deepcase(
        sentence=record[key_s1])
    s2_deep_list = check_deep_case_consistency.pic_up_deepcase(
        sentence=record[key_s2])

    if check_deep_case_consistency.are_arrays_equal(arr1=s1_deep_list, arr2=s2_deep_list):
        return 'exact_match'
    else:
        return 'not_exact_match'


def do_ensemble(
        make_file_or_path: MakeFileOrPath,
        read_file: ReadFile,
        key_id: str,
        key_s1: str,
        key_s2: str,
        key_true_label: str,
        key_withdeep_pred: str,
        key_nodeep_pred: str,
        key_ensembled_pred: str
) -> list:
    combined_json_path = make_file_or_path.make_combined_json_path_for_analysis()
    data = read_file.get_data(target_path=combined_json_path)

    result_json = []
    for record in data:
        exact_match_flag = check_deep_case_exact_match(
            record=record, key_s1=key_s1, key_s2=key_s2)

        # 深層格が完全一致だったら「深層格あり」の判定を使う場合
        if exact_match_flag == 'exact_match':
            result_record = {
                key_id: record[key_id],
                key_s1: record[key_s1],
                key_s2: record[key_s2],
                key_true_label: record[key_true_label],
                key_ensembled_pred: record[key_withdeep_pred]
            }
        else:
            result_record = {
                key_id: record[key_id],
                key_s1: record[key_s1],
                key_s2: record[key_s2],
                key_true_label: record[key_true_label],
                key_ensembled_pred: record[key_nodeep_pred]
            }

        result_json.append(result_record)

    return result_json


def main():
    # config_path = '../logAndResult/gpt-4o/ver1/part1/nodeep/config.yaml'
    config_path = "../logAndResult/jsnli/gpt-4o/nodeep/config.yaml"
    make_file_or_path = MakeFileOrPath(config_path=config_path)
    read_file = ReadFile(config_path=config_path)

    # keyの指定
    key_id = 'sentence_pair_id'
    key_s1 = 'sentence_1'
    key_s2 = 'sentence_2'
    key_true_label = 'true_label'
    key_withdeep_pred = 'withdeep_pred'
    key_nodeep_pred = 'nodeep_pred'
    key_ensembled_pred = 'key_ensembled_pred'

    result_json = do_ensemble(
        make_file_or_path=make_file_or_path,
        read_file=read_file,
        key_id=key_id,
        key_s1=key_s1,
        key_s2=key_s2,
        key_true_label=key_true_label,
        key_withdeep_pred=key_withdeep_pred,
        key_nodeep_pred=key_nodeep_pred,
        key_ensembled_pred=key_ensembled_pred
    )

    output_path = make_file_or_path.make_ensembled_json_path()
    make_file_or_path.make_output_json_file(
        result_dicts=result_json,
        output_path=output_path
    )

    calc_for_ensembled_json.calc_for_ensembled_json(
        config_path=config_path,
        read_file=read_file,
        make_file_or_path=make_file_or_path,
        key_true_label=key_true_label,
        key_ensembled_pred=key_ensembled_pred
    )


if __name__ == "__main__":
    main()
