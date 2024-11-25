import yaml


class MakeFilePath:
    def __init__(self, config_path: str):
        # 設定ファイルを読み込み
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        # output.jsonのパスを設定
        self.outputFile_path = config["openai"]["log_folder"] + \
            config["openai"]["output"]

    def make_outputFile_path(self):
        return self.outputFile_path
