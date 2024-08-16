import pandas as pd
import json
from collections import defaultdict

def denormalize_json(dataframe):
    """
    Преобразует DataFrame обратно в вложенный JSON-объект.

    :param dataframe: pandas DataFrame, который нужно преобразовать.
    :return: JSON-объект.
    """
    def nested_set(dic, keys, value):
        for key in keys[:-1]:
            if isinstance(dic, dict):
                dic = dic.setdefault(key, {})
            else:
                dic = {}
        dic[keys[-1]] = value

    def dict_to_defaultdict(d):
        if not isinstance(d, dict):
            return d
        return defaultdict(dict, {k: dict_to_defaultdict(v) for k, v in d.items()})

    records = dataframe.to_dict(orient='records')
    result = []

    for record in records:
        nested_record = dict_to_defaultdict({})
        for key, value in record.items():
            if 'Unnamed' in key:
                continue  # Пропускать ключи с 'Unnamed'
            keys = key.split('.')
            nested_set(nested_record, keys, value)
        result.append(nested_record)

    json_object = json.dumps(result, ensure_ascii=False, indent=4)
    return json_object
