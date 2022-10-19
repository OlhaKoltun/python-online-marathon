# Create function find(file, key)
# This function parses json-file and returns all unique values of the key.

import json


def find(file, key):
    with open(file, 'rb') as f:
        data = json.load(f)

    result = set()
    for item in find_keys_in_nested_dict(data, key):
        if isinstance(item, list):
            result.update(item)
        else:
            result.add(item)

    return list(result)


def find_keys_in_nested_dict(data, key):
    if isinstance(data, list):
        for item in data:
            for value in find_keys_in_nested_dict(item, key):
                yield value
    elif isinstance(data, dict):
        if key in data:
            yield data[key]
        for item in data.values():
            for value in find_keys_in_nested_dict(item, key):
                yield value
