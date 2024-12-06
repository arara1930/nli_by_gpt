from nli_by_gpt.use_gpt_api.make_file_path import MakeFilePath


def main():
    config_path = '../logAndResult/gpt-4o/part1/withdeep/config.yaml'
    # make_file_pathを初期化
    make_file_path = MakeFilePath(config_path)
    # combined.jsonのパスを指定
    combined_json_path_for_analysis = make_file_path.make_combined_json_path_for_analysis()
    # both_true.jsonのパスを指定
    both_true_path_for_analysis = make_file_path.make_both_true_path_for_analysis()
    # both_false.jsonのパスを指定
    both_false_path_for_analysis = make_file_path.make_both_false_path_for_analysis()
    # withdeep_only_true.jsonのパスを指定
    withdeep_only_true_path_for_analysis = make_file_path.make_withdeep_only_true_path_for_analysis()
    # nodeep_only_true.jsonのパスを指定
    nodeep_only_true_path_for_analysis = make_file_path.make_nodeep_only_true_path_for_analysis()


if __name__ == "__main__":
    main()
