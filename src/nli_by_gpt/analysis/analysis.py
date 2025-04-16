from nli_by_gpt.use_gpt_api.make_file_or_path import MakeFileOrPath
from nli_by_gpt.use_gpt_api.read_file import ReadFile
from nli_by_gpt.calc.calc import calc
from nli_by_gpt.calc.calc_for_combined_json import calc_for_combined_json
from nli_by_gpt.analysis.combine_result import combine
from nli_by_gpt.analysis.make_both_true_false_only_true_file import make_both_true_false_only_true_file


def append_to_result_txt(result_output_path: str, content_list: list):
    with open(result_output_path, 'a') as f:
        print('\n', file=f)
        for content in content_list:
            print(content, file=f)


def main():
    # config_path = "../logAndResult/gpt-4o/ver2/part1/nodeep/config.yaml"
    # config_path = "../logAndResult/gpt-4o/ver2/part1/withdeep/config.yaml"
    # config_path = "../logAndResult/gpt-4o-mini/ver1/part1/nodeep/config.yaml"
    # config_path = "../logAndResult/gpt-4o-mini/ver2/part1/withdeep/config.yaml"
    config_path = "../logAndResult/jsnli/gpt-4o/nodeep/config.yaml"

    # make_file_or_pathを初期化
    make_file_or_path = MakeFileOrPath(config_path)
    # output.jsonのパスを指定
    output_json_path = make_file_or_path.make_outputFile_path()
    # combined.jsonのパスを指定
    combined_json_path_for_analysis = make_file_or_path.make_combined_json_path_for_analysis()
    # both_true.jsonのパスを指定
    both_true_path_for_analysis = make_file_or_path.make_both_true_path_for_analysis()
    # both_false.jsonのパスを指定
    both_false_path_for_analysis = make_file_or_path.make_both_false_path_for_analysis()
    # withdeep_only_true.jsonのパスを指定
    withdeep_only_true_path_for_analysis = make_file_or_path.make_withdeep_only_true_path_for_analysis()
    # nodeep_only_true.jsonのパスを指定
    nodeep_only_true_path_for_analysis = make_file_or_path.make_nodeep_only_true_path_for_analysis()

    # ReadFileを初期化
    read_file = ReadFile(config_path=config_path)

    # 混合行列とクラシフィケーションレポートを作成
    calc(
        target_path=output_json_path,
        read_file=read_file,
        make_file_or_path=make_file_or_path
    )

    # combined.jsonを作成
    combine(make_file_or_path=make_file_or_path, read_file=read_file)

    # both_true,both_false,withdeep_only_true,nodeep_only_trueファイルを作成
    # result.txtに追記する内容をリストで返す
    list_for_append_result_txt = make_both_true_false_only_true_file(
        read_file=read_file,
        make_file_or_path=make_file_or_path,
        combined_json_path_for_analysis=combined_json_path_for_analysis,
        both_true_path_for_analysis=both_true_path_for_analysis,
        both_false_path_for_analysis=both_false_path_for_analysis,
        withdeep_only_true_path_for_analysis=withdeep_only_true_path_for_analysis,
        nodeep_only_true_path_for_analysis=nodeep_only_true_path_for_analysis
    )

    result_output_path = make_file_or_path.make_resultFile_path()
    # 上記の内容をresult.txtに追記
    append_to_result_txt(
        result_output_path=result_output_path,
        content_list=list_for_append_result_txt
    )

    # 各正答タイプ別jsonの混合行列とクラシフィケーションレポートをresult.txtに追記
    target_path_list = []
    target_path_list.append(
        {'path': withdeep_only_true_path_for_analysis, 'type': 'withdeep_only_true'})
    target_path_list.append(
        {'path': nodeep_only_true_path_for_analysis, 'type': 'nodeep_only_true'})
    calc_for_combined_json(
        target_path_list=target_path_list,
        read_file=read_file,
        make_file_or_path=make_file_or_path
    )


if __name__ == "__main__":
    main()
