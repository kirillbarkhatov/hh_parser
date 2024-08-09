import json


def json_reader(file_path: str) -> str:
    """Чтение JSON файла"""

    with open(file_path, "r") as file:
        return json.load(file)


if __name__ == "__main__":
    path = "/data/vacancies_example.json"
    print(json.dumps(json_reader(path), indent=4, ensure_ascii=False))
