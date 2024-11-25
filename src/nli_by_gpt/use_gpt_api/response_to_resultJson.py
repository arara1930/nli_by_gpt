import re
import read_file


class ProcessResponse:
    def __init__(self, response: str, sentence_pair_id: str, sentence1: str, sentence2: str, true_label: str):
        self.response = response
        self.sentence_pair_id = sentence_pair_id
        self.sentence1 = sentence1
        self.sentence2 = sentence2
        self.true_label = true_label

    def response_to_predLabel(self):
        response = self.response
        pattern_enttailment_1 = r'entailment'
        pattern_enttailment_2 = r'含意'
        pattern_contradiction_1 = r'contradiction'
        pattern_contradiction_2 = r'矛盾'
        pattern_neutral_1 = r'neutral'
        pattern_neutral_2 = r'中立'

        match_pattern_enttailment_1 = re.search(
            pattern_enttailment_1, response)
        match_pattern_enttailment_2 = re.search(
            pattern_enttailment_2, response)
        match_pattern_contradiction_1 = re.search(
            pattern_contradiction_1, response)
        match_pattern_contradiction_2 = re.search(
            pattern_contradiction_2, response)
        match_pattern_neutral_1 = re.search(pattern_neutral_1, response)
        match_pattern_neutral_2 = re.search(pattern_neutral_2, response)

        if match_pattern_enttailment_1 or match_pattern_enttailment_2:
            label = 'entailment'
        elif match_pattern_contradiction_1 or match_pattern_contradiction_2:
            label = 'contradiction'
        elif match_pattern_neutral_1 or match_pattern_neutral_2:
            label = 'neutral'
        else:
            label = 'unk'

        return label

    def process(self):
        pred_label = self.response_to_predLabel()
        result_record = {"sentence_pair_id": self.sentence_pair_id,
                         "sentence_1": self.sentence1,
                         "sentence_2": self.sentence2,
                         "true_label": self.true_label,
                         "pred_label": pred_label}
        return result_record


def main():
    config_path = "config.yaml"
    datas, key_id, key_s1, key_s2, key_true_label = read_file.read_file(
        config_path)
    response = '（含意）'
    processresponse = ProcessResponse(
        response=response,
        sentence_pair_id=datas[0][key_id],
        sentence1=datas[0][key_s1],
        sentence2=datas[0][key_s2],
        true_label=datas[0][key_true_label])
    result_record = processresponse.process()

    print(result_record)


if __name__ == "__main__":
    main()
