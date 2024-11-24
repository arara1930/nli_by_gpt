import json


def make_prompt(s1: str, s2: str):
    prompt = (
        f"#ロール#\n"
        f"あなたは含意関係認識が得意な大学教授です。\n"
        f"#指示#\n"
        f"#前提文#に対する#仮定文#の含意関係が、「entailment（含意）」「contradiction（矛盾）」「neutral（中立）」のどれであるか、以下に示す#定義#を参考に判定せよ。また判定の際、「書かれていない情報」を根拠にしないように注意せよ。\n"
        f"また、答えは#判定#だけを出力してください。\n"
        f"#定義#\n"
        f"entailment（含意）:前提文が真であるとき、仮定文も真になる場合\n"
        f"contradiction（矛盾）:前提文が真であるとき、仮定文が偽になる場合\n"
        f"neutral（中立）:含意と矛盾のどちらにも当てはまらない場合\n"
        f"#前提文#\n"
        f"{s1}\n"
        f"#仮定文#\n"
        f"{s2}\n"
        f"#判定#\n"
    )
    return prompt


def main():
    # ファイルを開いてJSONデータを読み込む
    with open('datas/text_deepCased_sentences.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    prompt = make_prompt(data[0]['sentence_1'], data[0]['sentence_2'])
    print(prompt)


if __name__ == "__main__":
    main()
