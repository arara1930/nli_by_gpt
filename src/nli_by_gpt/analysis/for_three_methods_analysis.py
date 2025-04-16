import json
from nli_by_gpt.use_gpt_api.make_file_or_path import MakeFileOrPath
from nli_by_gpt.use_gpt_api.read_file import ReadFile
from nli_by_gpt.analysis.combine_result import combine_for_three_methods
from nli_by_gpt.analysis.make_both_true_false_only_true_file import make_only_true_file_for_three_methods


def main():
    config_path = "../logAndResult/gpt-4o/ver2/part1/nodeep/config.yaml"
    # config_path = "../logAndResult/gpt-4o/ver2/part1/nodeep/config.yaml"

    # make_file_or_pathを初期化
    make_file_or_path = MakeFileOrPath(config_path)
    # ReadFileを初期化
    read_file = ReadFile(config_path=config_path)

    # combined.jsonのパスを指定
    combined_json_path_for_analysis = make_file_or_path.make_combined_for_three_methods_json_path_for_analysis()
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

    # # 3手法の結果を一つのjsonにまとめる
    # combine_for_three_methods(
    #     make_file_or_path=make_file_or_path, read_file=read_file)

    # 深層格ありなし(アンサンブル)の○×混合行列を総当たりで計4種類作成しanalysis/for_three_methods/result.txtに保存
    # 深層格ありなし(アンサンブル)のjsonを作成
    make_only_true_file_for_three_methods(
        read_file=read_file,
        make_file_or_path=make_file_or_path,
        combined_json_path_for_analysis=combined_json_path_for_analysis,
        all_true_path_for_analysis=all_true_path_for_analysis,
        all_false_path_for_analysis=all_false_path_for_analysis,
        withdeep_only_true_path_for_analysis=withdeep_only_true_path_for_analysis,
        withdeep_ensemble_true_path_for_analysis=withdeep_ensemble_true_path_for_analysis,
        nodeep_only_true_path_for_analysis=nodeep_only_true_path_for_analysis,
        nodeep_ensemble_true_path_for_analysis=nodeep_ensemble_true_path_for_analysis
    )


if __name__ == "__main__":
    main()
