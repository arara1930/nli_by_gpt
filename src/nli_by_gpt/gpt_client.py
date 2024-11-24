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

        # ログファイルのパスを設定
        self.log_data = config["openai"]["log_folder"] + \
            config["openai"]["log_file"]

    def generate_completion(self, messages, model=None):
        """
        メッセージを送信してAIの応答を取得
        """
        success = False  # 成功したかどうかのフラ
        while not success:  # 成功するまでループ
            try:
                response_list = []
                client = self.client
                # デフォルトモデルを使用
                model = model or self.model
                stream = client.chat.completions.create(
                    model=model,
                    messages=messages,
                    stream=True
                )
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        response_list .append(chunk.choices[0].delta.content)
                response = ''.join(response_list)

                # もし上記の処理が成功したら、successフラグをTrueに変更
                success = True

                with open(self.log_data, 'a') as f:
                    print(response, file=f)

                return response
            except Exception as e:
                with open(self.log_data, 'a') as f:
                    print(f"An error occurred: {e}", file=f)
                    print("Sleeping for 5 s before retrying...", file=f)
                print(f"An error occurred: {e}")
                print("Sleeping for 5 s before retrying...")
                time.sleep(5)  # 5秒停止