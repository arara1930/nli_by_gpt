from sklearn.metrics import classification_report, confusion_matrix
import yaml
import read_file


def make_true_pred_list(datas: list, key_true_label: str, key_pred_label: str):
    true_label = []
    for record in datas:
        true_label.append(record[key_true_label])
    pred_label = []
    for record in datas:
        pred_label.append(record[key_pred_label])

    return true_label, pred_label


def use_classification_report(config_path: str):
    result_output_path, datas, key_id, key_s1, key_s2, key_true_label, key_pred_label = read_file.read_jsonFile(
        config_path)

    true_label, pred_label = make_true_pred_list(
        datas=datas, key_true_label=key_true_label, key_pred_label=key_pred_label)

    print(classification_report(true_label, pred_label))

    with open(result_output_path, 'a') as f:
        print(classification_report(true_label, pred_label), file=f)


def use_confusion_matrix(config_path: str):
    result_output_path, datas, key_id, key_s1, key_s2, key_true_label, key_pred_label = read_file.read_jsonFile(
        config_path)

    true_label, pred_label = make_true_pred_list(
        datas=datas, key_true_label=key_true_label, key_pred_label=key_pred_label)

    print(confusion_matrix(true_label, pred_label))

    with open(result_output_path, 'a') as f:
        print(confusion_matrix(true_label, pred_label), file=f)


def main():
    config_path = "../logAndResult/gpt-4o-mini/part1/nodeep/config.yaml"
    use_classification_report(config_path=config_path)
    use_confusion_matrix(config_path=config_path)


if __name__ == "__main__":
    main()
