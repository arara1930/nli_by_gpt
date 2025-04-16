from nli_by_gpt.use_gpt_api.make_file_or_path import MakeFileOrPath
from nli_by_gpt.use_gpt_api.read_file import ReadFile
from nli_by_gpt.analysis.check_deep_case_consistency import count_and_print_deep_case_consistency_num


def main():
    config_path = "../logAndResult/gpt-4o/fewshot_ver1/part1/withdeep/config.yaml"

    # make_file_or_pathを初期化
    make_file_or_path = MakeFileOrPath(config_path)
    # output.jsonのパスを指定
    output_json_path = make_file_or_path.make_outputFile_path()

    # ReadFileを初期化
    read_file = ReadFile(config_path=config_path)
    data, key_id, key_s1, key_s2, key_true_label = read_file.get_jsonFile_keys()
    print(data[0])

    


if __name__ == "__main__":
    main()
