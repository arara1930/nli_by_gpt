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


def use_classification_report(target_path: str, read_file: ReadFile, make_file_or_path: MakeFileOrPath) -> None:
    result_output_path = make_file_or_path.make_resultFile_path()
    datas, key_id, key_s1, key_s2, key_true_label, key_pred_label, key_log = read_file.get_jsonFile_keys_for_analysis(
        target_path)

    true_label, pred_label = make_true_pred_list(
        datas=datas, key_true_label=key_true_label, key_pred_label=key_pred_label)

    print(classification_report(true_label, pred_label))

    with open(result_output_path, 'a') as f:
        print(classification_report(true_label, pred_label), file=f)


def use_confusion_matrix(target_path: str, read_file: ReadFile, make_file_or_path: MakeFileOrPath) -> None:
    result_output_path = make_file_or_path.make_resultFile_path()
    datas, key_id, key_s1, key_s2, key_true_label, key_pred_label, key_log = read_file.get_jsonFile_keys_for_analysis(
        target_path)

    true_label, pred_label = make_true_pred_list(
        datas=datas, key_true_label=key_true_label, key_pred_label=key_pred_label)

    print(confusion_matrix(true_label, pred_label))

    with open(result_output_path, 'a') as f:
        print(confusion_matrix(true_label, pred_label), file=f)


def calc(target_path: str, read_file: ReadFile, make_file_or_path: MakeFileOrPath):
    use_classification_report(
        target_path=target_path,
        read_file=read_file,
        make_file_or_path=make_file_or_path
    )
    use_confusion_matrix(
        target_path=target_path,
        read_file=read_file,
        make_file_or_path=make_file_or_path
    )


def main():
    config_path = "../logAndResult/gpt-4.1/fewshot_ver2/part1/nodeep/config.yaml"
    target_json_path = '../logAndResult/gpt-4.1/fewshot_ver2/part1/nodeep/output.json'
    read_file = ReadFile(config_path=config_path)
    make_file_or_path = MakeFileOrPath(config_path)
    calc(
        target_path=target_json_path,
        read_file=read_file,
        make_file_or_path=make_file_or_path
    )


if __name__ == "__main__":
    main()
