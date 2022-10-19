# Function user_with_department(csv_file, user_json, department_json) should read from json files information and create csv file in format:
# header line - user, department
# next lines :  <userName>, <departmentName>

import json
import jsonschema
from jsonschema import validate
import csv


class InvalidInstanceError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Error in {self.data} schema"


class DepartmentName(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Department with id {self.data} doesn't exists"


user_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "department_id": {"type": "number"},
        },
        "required": ["department_id"],
    }
}

department_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
        },
        "required": ["id"],
    }
}


def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema, )
        return True
    except jsonschema.exceptions.ValidationError:
        raise InvalidInstanceError("user" if schema == user_schema else "department")


def user_with_department(csv_file, user_json, department_json):
    with open(user_json, 'rb') as user_file, open(department_json, 'rb') as department_file:
        users = json.load(user_file)
        departments = json.load(department_file)

    result = []
    if validate_json(users, user_schema) and validate_json(departments, department_schema):
        all_department_id = set(department["id"] for department in departments)
        for user in users:
            try:
                if user["department_id"] in all_department_id:
                    for department in departments:
                        if department["id"] == user["department_id"]:
                            result.append({"name": user["name"], "department": department["name"]})
                else:
                    raise DepartmentName(user["department_id"])
            except DepartmentName as e:
                print(e)
    fields = ['name', 'department']
    with open(csv_file, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(result)
