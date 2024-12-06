import yaml


class MakeFilePath:
    def __init__(self, config_path: str):
        # 設定ファイルを読み込み
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

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

    def make_outputFile_path(self):
        return self.outputFile_path

    def make_inputFile_path(self):
        return self .inputFile_path

    def make_set_up_of_test_txt_path(self):
        return self.set_up_of_test_txt_path

    def make_outputFile_withdeep_path_for_analysis(self):
        return self.outputFile_withdeep_path_for_analysis

    def make_outputFile_nodeep_path_for_analysis(self):
        return self.outputFile_nodeep_path_for_analysis
