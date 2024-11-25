from gpt_client import GPTClient
from response_to_resultJson import ProcessResponse
from make_file_path import MakeFilePath
import read_file
import json
from tqdm import tqdm


def make_prompt(s1: str, s2: str):
    # # 深層格ありver
    # prompt = (
    #     f"#指示#\n"
    #     f"#前提文#に対する#仮定文#の含意関係が、「entailment（含意）」「contradiction（矛盾）」「neutral（中立）」のどれであるか、以下に示す#定義#を参考に判定せよ。\n"
    #     f"また、#注意#に書かれている内容に留意せよ。\n"
    #     f"#定義#\n"
    #     f"entailment（含意）:前提文が真であるとき、仮定文も真になる場合\n"
    #     f"contradiction（矛盾）:前提文が真であるとき、仮定文が偽になる場合\n"
    #     f"neutral（中立）:含意と矛盾のどちらにも当てはまらない場合\n"
    #     f"#注意#\n"
    #     f"1つ目：#前提文#と#仮定文#の双方に<>で囲われたタグがあるが、述語と名詞の意味的な関係を表す文法上のカテゴリーである深層格を示している。この深層格も根拠として判定せよ。\n"
    #     f"2つ目：判定の際、「書かれていない情報」を根拠に判定することがないように注意せよ。\n"
    #     f"3つ目：答えは#判定#だけを出力せよ。\n"
    #     f"#前提文#\n"
    #     f"{s1}\n"
    #     f"#仮定文#\n"
    #     f"{s2}\n"
    #     f"#判定#\n"
    # )

    # 深層格なしver
    prompt = (
        f"#指示#\n"
        f"#前提文#に対する#仮定文#の含意関係が、「entailment（含意）」「contradiction（矛盾）」「neutral（中立）」のどれであるか、以下に示す#定義#を参考に判定せよ。\n"
        f"また、#注意#に書かれている内容に留意せよ。\n"
        f"#定義#\n"
        f"entailment（含意）:前提文が真であるとき、仮定文も真になる場合\n"
        f"contradiction（矛盾）:前提文が真であるとき、仮定文が偽になる場合\n"
        f"neutral（中立）:含意と矛盾のどちらにも当てはまらない場合\n"
        f"#注意#\n"
        f"1つ目：判定の際、「書かれていない情報」を根拠に判定することがないように注意せよ。\n"
        f"2つ目：答えは#判定#だけを出力せよ。\n"
        f"#前提文#\n"
        f"{s1}\n"
        f"#仮定文#\n"
        f"{s2}\n"
        f"#判定#\n"
    )

    return prompt


def main():
    # クライアントを初期化
    config_path = "../config.yaml"
    client = GPTClient(config_path)

    datas, key_id, key_s1, key_s2, key_true_label = read_file.read_file(
        config_path)

    roop_num = 0
    result_dicts = []
    for record in tqdm(datas, desc="Processing Data", unit="item"):
        # ユーザーの入力
        user_input = make_prompt(record[key_s1], record[key_s2])

        # メッセージを送信
        messages = [
            {"role": "system", "content": "あなたは含意関係認識が得意な大学教授です。"},
            {"role": "user", "content": user_input}
        ]
        try:
            response = client.generate_completion(messages)
            # print("AIの応答:")
            # print(response)
            processresponse = ProcessResponse(
                response=response,
                sentence_pair_id=record[key_id],
                sentence1=record[key_s1],
                sentence2=record[key_s2],
                true_label=record[key_true_label])
            result_record = processresponse.process()
            result_dicts.append(result_record)
        except RuntimeError as e:
            print(f"エラー: {e}")

        # roop_num += 1
        # if roop_num == 2:
        #     break

    make_file_path = MakeFilePath(config_path)
    output_path = make_file_path.make_outputFile_path()

    # JSON形式の文字列に変換
    json_data = json.dumps(result_dicts, ensure_ascii=False, indent=4)

    # ファイルに書き出す
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(json_data)


if __name__ == "__main__":
    main()