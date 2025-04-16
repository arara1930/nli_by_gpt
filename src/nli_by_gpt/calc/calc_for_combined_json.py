from sklearn.metrics import classification_report, confusion_matrix
import yaml
from nli_by_gpt.use_gpt_api.read_file import ReadFile
from nli_by_gpt.use_gpt_api.make_file_or_path import MakeFileOrPath


def make_true_pred_list(datas: list, key_true_label: str, key_pred_label: str) -> str:
    true_label = []
    for record in datas:
        true_label.append(record[key_true_label])
    pred_label = []
    for record in datas:
        pred_label.append(record[key_pred_label])

    return true_label, pred_label


# def use_classification_report(target_path: str, read_file: ReadFile, make_file_or_path: MakeFileOrPath) -> None:
#     result_output_path = make_file_or_path.make_resultFile_path()
#     datas, key_id, key_s1, key_s2, key_true_label, key_withdeep_pred_label, key_nodeep_pred_label = read_file.get_jsonFile_keys_for_analysis_combied_json(
#         target_path)

#     true_label, pred_label = make_true_pred_list(
#         datas=datas, key_true_label=key_true_label, key_pred_label=key_pred_label)

#     print(target_path)
#     print(classification_report(true_label, pred_label))

#     with open(result_output_path, 'a') as f:
#         print('\n')
#         print(target_path)
#         print(classification_report(true_label, pred_label), file=f)


def use_confusion_matrix(target_path: str, target_type: str, read_file: ReadFile, make_file_or_path: MakeFileOrPath) -> None:
    result_output_path = make_file_or_path.make_resultFile_path()
    datas, key_id, key_s1, key_s2, key_true_label, key_withdeep_pred_label, key_nodeep_pred_label = read_file.get_jsonFile_keys_for_analysis_combied_json(
        target_path)

    if target_type == 'withdeep_only_true':
        true_label, pred_label = make_true_pred_list(
            datas=datas, key_true_label=key_true_label, key_pred_label=key_nodeep_pred_label)
    elif target_type == 'nodeep_only_true':
        true_label, pred_label = make_true_pred_list(
            datas=datas, key_true_label=key_true_label, key_pred_label=key_withdeep_pred_label)

    print(target_type)
    print(confusion_matrix(true_label, pred_label))

    with open(result_output_path, 'a') as f:
        print('\n', file=f)
        print(target_type, file=f)
        print(confusion_matrix(true_label, pred_label), file=f)


def calc_for_combined_json(target_path_list: list, read_file: ReadFile, make_file_or_path: MakeFileOrPath):
    for target_path in target_path_list:
        # use_classification_report(
        #     target_path=target_path,
        #     read_file=read_file,
        #     make_file_or_path=make_file_or_path
        # )
        use_confusion_matrix(
            target_path=target_path['path'],
            target_type=target_path['type'],
            read_file=read_file,
            make_file_or_path=make_file_or_path
        )


def main():
    config_path = "../../logAndResult/llm_jp_13b_instruct_full_jaster_v1.0/part1/nodeep/config.yaml"
    read_file = ReadFile(config_path=config_path)
    make_file_or_path = MakeFileOrPath(config_path)


if __name__ == "__main__":
    main()
