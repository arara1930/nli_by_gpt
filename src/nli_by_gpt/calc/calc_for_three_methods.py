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


def use_confusion_matrix(
        target_path: str,
        read_file: ReadFile,
        make_file_or_path: MakeFileOrPath,
        key_true_label: str,
        key_error_pred_label: str
) -> None:
    result_output_path = make_file_or_path.make_resultFile_for_three_methods_path()
    datas = read_file.get_data(target_path)

    true_label, pred_label = make_true_pred_list(
        datas=datas, key_true_label=key_true_label, key_pred_label=key_error_pred_label)

    print(confusion_matrix(true_label, pred_label))

    with open(result_output_path, 'a') as f:
        print(target_path, file=f)
        print(confusion_matrix(true_label, pred_label), file=f)
        print('\n')


def calc_for_three_methods(
        target_path: str,
        read_file: ReadFile,
        make_file_or_path: MakeFileOrPath,
        key_true_label: str,
        key_error_pred_label: str
):

    use_confusion_matrix(
        target_path=target_path,
        read_file=read_file,
        make_file_or_path=make_file_or_path,
        key_true_label=key_true_label,
        key_error_pred_label=key_error_pred_label
    )


def main():
    config_path = "../logAndResult/gpt-4o/ver2/part1/nodeep/config.yaml"
    read_file = ReadFile(config_path=config_path)
    make_file_or_path = MakeFileOrPath(config_path)

    # all_true.jsonのパスを指定
    all_true_path_for_analysis = make_file_or_path.make_all_true_path_for_three_methods()
    # all_false.json
    all_false_path_for_analysis = make_file_or_path.make_all_false_path_for_three_methods()
    # withdeep_only_true.jsonのパスを指定
    withdeep_only_true_path_for_analysis = make_file_or_path.make_withdeep_only_true_path_for_three_methods()
    # withdeep_ensemble_true.jsonのパスを指定
    withdeep_ensemble_true_path_for_analysis = make_file_or_path.make_withdeep_ensemble_true_path_for_three_methods()
    # nodeep_only_true.jsonのパスを指定
    nodeep_only_true_path_for_analysis = make_file_or_path.make_nodeep_only_true_path_for_three_methods()
    # nodeep_ensemble_true.jsonのパスを指定
    nodeep_ensemble_true_path_for_analysis = make_file_or_path.make_nodeep_ensemble_true_path_for_three_methods()

    # keyの指定
    key_id = 'sentence_pair_id'
    key_s1 = 'sentence_1'
    key_s2 = 'sentence_2'
    key_true_label = 'true_label'
    key_error_pred_label = 'error_pred_label'
    key_withdeep_pred = 'withdeep_pred'
    key_nodeep_pred = 'nodeep_pred'
    key_ensembled_pred = 'key_ensembled_pred'

    for target_path in [
        all_true_path_for_analysis,
        all_false_path_for_analysis,
        withdeep_only_true_path_for_analysis,
        withdeep_ensemble_true_path_for_analysis,
        nodeep_only_true_path_for_analysis,
        nodeep_ensemble_true_path_for_analysis
    ]:
        calc_for_three_methods(
            target_path=target_path,
            read_file=read_file,
            make_file_or_path=make_file_or_path,
            key_true_label=key_true_label,
            key_error_pred_label=key_error_pred_label
        )


if __name__ == "__main__":
    main()
