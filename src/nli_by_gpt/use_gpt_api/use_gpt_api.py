from gpt_client import GPTClient
from response_to_resultJson import ProcessResponse
from nli_by_gpt.use_gpt_api.make_file_or_path import MakeFileOrPath
from read_file import ReadFile
from nli_by_gpt.use_gpt_api import make_prompt
import json
from tqdm import tqdm


def make_set_up_of_test_txt(output_path: str, input_file_path: str, user_input: str):
    with open(output_path, 'a') as f:
        print('入力データ', file=f)
        print(input_file_path, file=f)
        print('プロンプト', file=f)
        print(user_input, file=f)


def main():
    # クライアントを初期化
    # config_path = "../logAndResult/gpt-4o/fewshot_ver1/part1/nodeep/config.yaml"
    # config_path = "../logAndResult/gpt-4o/fewshot_ver3/part1/withdeep/config.yaml"
    config_path = "../logAndResult/o3-mini/fewshot_ver1/part1/nodeep/config.yaml"
    # config_path = "../logAndResult/o3-mini/zeroshot_ver2/part1/nodeep/config.yaml"
    # config_path = "../logAndResult/gpt-4o-mini/ver2/part1/nodeep/config.yaml"
    # config_path = "../logAndResult/gpt-4o-mini/ver2/part1/withdeep/config.yaml"
    # config_path = "../logAndResult/jsnli/gpt-4o/withdeep/config.yaml"

    client = GPTClient(config_path)

    read_file = ReadFile(config_path)
    config = read_file.get_config()
    use_prompt_ver = config['openai']['use_prompt_ver']
    datas, key_id, key_s1, key_s2, key_true_label = read_file.get_jsonFile_keys()

    # deep_or_no_deep_flagフラグの格納
    deep_or_no_deep_flag = config['openai']['deep_or_no_deep_flag']

    # 以下、実験設定の記録に使用
    # make_file_or_pathを初期化
    make_file_or_path = MakeFileOrPath(config_path)
    # テストに使う元データのパスを設定
    inputFile_path = make_file_or_path.make_inputFile_path()
    # set_up_of_test.txtのパスを設定
    set_up_of_test_txt_path = make_file_or_path.make_set_up_of_test_txt_path()

    roop_num = 0
    result_dicts = []
    for record in tqdm(datas, desc="Processing Data", unit="item"):
        # ユーザーの入力
        user_input = make_prompt.make_prompt(
            record[key_s1],
            record[key_s2],
            deep_or_no_deep_flag,
            use_prompt_ver=use_prompt_ver
        )

        # メッセージを送信
        # messages = [
        #     {"role": "system", "content": "あなたは含意関係認識が得意な大学教授です。"},
        #     {"role": "user", "content": user_input}
        # ]
        messages = [
            {"role": "user", "content": user_input}
        ]

        # # for o1
        # messages = [
        #     {"role": "user", "content": user_input}
        # ]

        # 実験に用いたデータセットとプロンプトを格納
        if roop_num == 0:
            make_file_or_path.make_set_up_of_test_txt(user_input=user_input)

        try:
            response, log_list = client.generate_completion(messages)
            # print("AIの応答:")
            # print(response)
            processresponse = ProcessResponse(
                response=response,
                log_list=log_list,
                sentence_pair_id=record[key_id],
                sentence1=record[key_s1],
                sentence2=record[key_s2],
                true_label=record[key_true_label])
            result_record = processresponse.process()
            result_dicts.append(result_record)
        except RuntimeError as e:
            print(f"エラー: {e}")

        roop_num += 1

        # if roop_num == 1:
        #     break

        if roop_num % 500 == 0:
            # 500件推論完了ごとにファイルを出力
            output_path = make_file_or_path.make_outputFile_on_the_way_path(
                current_id=record[key_id])
            make_file_or_path.make_output_json_file(
                result_dicts=result_dicts, output_path=output_path)

    # roop_numが1の時はjsonファイルを出力しない
    # 1件も処理していない場合は終了
    if roop_num == 1:
        output_path = "../logAndResult/o3-mini/fewshot_ver1/part1/nodeep/test.json"
    else:
        output_path = make_file_or_path.make_outputFile_path()

    # JSON形式の文字列に変換
    json_data = json.dumps(result_dicts, ensure_ascii=False, indent=4)

    # ファイルに書き出す
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(json_data)


if __name__ == "__main__":
    main()
