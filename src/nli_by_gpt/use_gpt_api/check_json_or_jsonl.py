import json


def detect_file_format(file_path):
    try:
        # ファイル全体を読み込んでJSONとして解析を試みる
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return "JSON"
    except json.JSONDecodeError:
        try:
            # 各行を個別にJSONとして解析を試みる
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    json.loads(line)
            return "JSONL"
        except json.JSONDecodeError:
            return "Invalid format"


def main():
    file_path = "../../../../datas/jnli-valid-v1.1.json"  # または "example.jsonl"
    result = detect_file_format(file_path)
    print(f"The file format is: {result}")


if __name__ == "__main__":
    main()
