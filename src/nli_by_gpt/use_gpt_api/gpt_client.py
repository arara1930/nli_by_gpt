import yaml
from openai import OpenAI
import time


class GPTClient:
    def __init__(self, config_path: str):
        # 設定ファイルを読み込み
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        # APIキーを設定
        self.client = OpenAI(api_key=config["openai"]["api_key"])

        # デフォルトモデルを設定
        self.model = config["openai"]["model"]

        # temperatureを設定
        self.temperature = config["openai"]["temperature"]

        # レスポンスログファイルのパスを設定
        self.res_log_data = config["openai"]["log_folder"] + \
            config["openai"]["res_log_file"]

        # レスポンスラベルログファイルのパスを設定
        self.res_label_log_file = config["openai"]["log_folder"] + \
            config["openai"]["res_label_log_file"]

    def generate_completion(self, messages, model=None):
        """
        メッセージを送信してAIの応答を取得
        """
        log_list = []  # データそれぞれに対するログを格納
        success = False  # 成功したかどうかのフラグ
        while not success:  # 成功するまでループ
            try:
                response_list = []
                client = self.client
                # デフォルトモデルを使用
                model = model or self.model
                stream = client.chat.completions.create(
                    model=model,
                    temperature=self.temperature,  # o1を使う時はコメントアウト
                    messages=messages,
                    stream=True
                )
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        response_list .append(chunk.choices[0].delta.content)
                response = ''.join(response_list)
                log_list.append(response)
                # もし上記の処理が成功したら、successフラグをTrueに変更
                success = True

                # with open(self.res_log_data, 'a') as f:
                #     print(response, file=f)

                # with open(self.res_label_log_file, 'a') as f:
                #     print(response, file=f)

                return response, log_list
            except Exception as e:
                with open(self.res_log_data, 'a') as f:
                    print(f"An error occurred: {e}", file=f)
                    print("Sleeping for 5 s before retrying...", file=f)
                print(f"An error occurred: {e}")
                print("Sleeping for 5 s before retrying...")
                time.sleep(5)  # 5秒停止
