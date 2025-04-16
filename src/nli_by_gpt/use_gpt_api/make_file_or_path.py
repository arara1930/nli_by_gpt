import yaml
import json


class MakeFileOrPath:
    def __init__(self, config_path: str):
        # 設定ファイルを読み込み
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
            self.config = config

        # output.jsonのパスを設定
        self.outputFile_path = config["openai"]["log_folder"] + \
            config["openai"]["output"]

        # テストに使う元データのパスを設定
        self.inputFile_path = config["openai"]["input"]

        # set_up_of_test.txtのパスを設定
        self.set_up_of_test_txt_path = config["openai"]["log_folder"] + \
            config["openai"]["set_up_of_test_txt"]

        # output.jsonのパスを指定(analysis用、withdeep)
        self.outputFile_withdeep_path_for_analysis = config["analysis"]['withdeep']["log_folder"] + \
            config["analysis"]['withdeep']["output"]

        # output.jsonのパスを指定(analysis用、nodeep)
        self.outputFile_nodeep_path_for_analysis = config["analysis"]['nodeep']["log_folder"] + \
            config["analysis"]['nodeep']["output"]

        # output.jsonのパスを指定(analysis用、nodeep)
        self.outputFile_ensembled_path_for_analysis = config["ensemble"]["log_folder"] + \
            config["ensemble"]["output"]

        # result.txtのパスを指定
        self.resultFile_path = config["openai"]["log_folder"] + \
            config["calc"]["result_file"]

        # ensembleのresult.txtのパスを指定
        self.resultFile_for_ensembled_path = config["ensemble"]["log_folder"] + \
            config["calc"]["result_file"]

        # for_three_methodsのresult.txtのパスを指定
        self.resultFile_for_three_methods_path = config["analysis"]["analysis_path_for_three_methods"]["log_folder"] + \
            config["calc"]["result_file"]

        # combined.jsonのパスを指定
        self.combined_json_path_for_analysis = config["analysis"]['analysis_path']["log_folder"] + \
            config["analysis"]['analysis_path']["combined"]

        # both_true.jsonのパスを指定
        self.both_true_path_for_analysis = config["analysis"]['analysis_path']["log_folder"] + \
            config["analysis"]['analysis_path']["both_true"]

        # both_false.jsonのパスを指定
        self.both_false_path_for_analysis = config["analysis"]['analysis_path']["log_folder"] + \
            config["analysis"]['analysis_path']["both_false"]

        # withdeep_only_true.jsonのパスを指定
        self.withdeep_only_true_path_for_analysis = config["analysis"]['analysis_path']["log_folder"] + \
            config["analysis"]['analysis_path']["withdeep_only_true"]

        # nodeep_only_true.jsonのパスを指定
        self.nodeep_only_true_path_for_analysis = config["analysis"]['analysis_path']["log_folder"] + \
            config["analysis"]['analysis_path']["nodeep_only_true"]

        # all_true.jsonのパスを指定(for_three_methods)
        self.all_true_path_for_three_methods = config["analysis"]['analysis_path_for_three_methods']["log_folder"] + \
            config["analysis"]['analysis_path_for_three_methods']["all_true"]

        # all_false.jsonのパスを指定(for_three_methods)
        self.all_false_path_for_three_methods = config["analysis"]['analysis_path_for_three_methods']["log_folder"] + \
            config["analysis"]['analysis_path_for_three_methods']["all_false"]

        # withdeep_only_true.jsonのパスを指定(for_three_methods)
        self.withdeep_only_true_path_for_three_methods = config["analysis"]['analysis_path_for_three_methods']["log_folder"] + \
            config["analysis"]['analysis_path_for_three_methods']["withdeep_only_true"]

        # withdeep_ensemble_true.jsonのパスを指定(for_three_methods)
        self.withdeep_ensemble_true_path_for_three_methods = config["analysis"]['analysis_path_for_three_methods']["log_folder"] + \
            config["analysis"]['analysis_path_for_three_methods']["withdeep_ensemble_true"]

        # nodeep_only_true.jsonのパスを指定(for_three_methods)
        self.nodeep_only_true_path_for_three_methods = config["analysis"]['analysis_path_for_three_methods']["log_folder"] + \
            config["analysis"]['analysis_path_for_three_methods']["nodeep_only_true"]

        # nodeep_ensemble_true.jsonのパスを指定(for_three_methods)
        self.nodeep_ensemble_true_path_for_three_methods = config["analysis"]['analysis_path_for_three_methods']["log_folder"] + \
            config["analysis"]['analysis_path_for_three_methods']["nodeep_ensemble_true"]

        # combined.json for three methodsのパスを指定
        self.combined_for_three_methods_json_path_for_analysis = config[
            "analysis"]['withdeep']["combined_for_three_methods"]

        # ensembled.jsonのパスを指定
        self.ensembled_json_path = config["ensemble"]["log_folder"] + \
            config["ensemble"]["output"]

    def make_outputFile_on_the_way_path(self, current_id: str):
        outputFile_path = self.config['openai']['log_folder'] + \
            f'output_{current_id}.json'
        return outputFile_path

    def make_outputFile_path(self):
        return self.outputFile_path

    def make_inputFile_path(self):
        return self.inputFile_path

    def make_set_up_of_test_txt_path(self):
        return self.set_up_of_test_txt_path

    def make_outputFile_withdeep_path_for_analysis(self):
        return self.outputFile_withdeep_path_for_analysis

    def make_outputFile_nodeep_path_for_analysis(self):
        return self.outputFile_nodeep_path_for_analysis

    def make_outputFile_ensembled_path_for_analysis(self):
        return self.outputFile_ensembled_path_for_analysis

    def make_resultFile_path(self) -> str:
        return self.resultFile_path

    def make_resultFile_for_ensembled_path(self) -> str:
        return self.resultFile_for_ensembled_path

    def make_resultFile_for_three_methods_path(self) -> str:
        return self.resultFile_for_three_methods_path

    def make_combined_json_path_for_analysis(self):
        return self.combined_json_path_for_analysis

    def make_both_true_path_for_analysis(self):
        return self.both_true_path_for_analysis

    def make_both_false_path_for_analysis(self):
        return self.both_false_path_for_analysis

    def make_withdeep_only_true_path_for_analysis(self):
        return self.withdeep_only_true_path_for_analysis

    def make_nodeep_only_true_path_for_analysis(self):
        return self.nodeep_only_true_path_for_analysis

    def make_all_true_path_for_three_methods(self):
        return self.all_true_path_for_three_methods

    def make_all_false_path_for_three_methods(self):
        return self.all_false_path_for_three_methods

    def make_withdeep_only_true_path_for_three_methods(self):
        return self.withdeep_only_true_path_for_three_methods

    def make_withdeep_ensemble_true_path_for_three_methods(self):
        return self.withdeep_ensemble_true_path_for_three_methods

    def make_nodeep_only_true_path_for_three_methods(self):
        return self.nodeep_only_true_path_for_three_methods

    def make_nodeep_ensemble_true_path_for_three_methods(self):
        return self.nodeep_ensemble_true_path_for_three_methods

    def make_combined_for_three_methods_json_path_for_analysis(self):
        return self.combined_for_three_methods_json_path_for_analysis

    def make_ensembled_json_path(self):
        return self.ensembled_json_path

    def make_set_up_of_test_txt(self, user_input: str):
        with open(self.set_up_of_test_txt_path, 'a') as f:
            print('入力データ', file=f)
            print(self.inputFile_path, file=f)
            print('\n', file=f)
            print(
                '####################################################################', file=f)
            print('\n', file=f)
            print('プロンプト', file=f)
            print(user_input, file=f)

    def make_output_json_file(self, result_dicts: list, output_path: str):
        # JSON形式の文字列に変換
        json_data = json.dumps(result_dicts, ensure_ascii=False, indent=4)

        # ファイルに書き出す
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(json_data)
