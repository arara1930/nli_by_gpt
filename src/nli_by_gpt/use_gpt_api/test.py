import json
import re
from gpt_client import GPTClient
import read_file


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

    user_input = make_prompt(datas[0][key_s1], datas[0][key_s2])
    print(user_input)


if __name__ == "__main__":
    main()
