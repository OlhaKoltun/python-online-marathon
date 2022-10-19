# Class Student has attributes full_name:str, avg_rank: float, courses: list
# Class Group has attributes title: str, students: list.
# Make both classes JSON serializable. 
# Json-files represent information about student (students). 
# Create methods:  
# Student.from_json(json_file) that return Student instance from attributes from json-file;
# Group.serialize_to_json(list_of_groups, filename)
# Group.create_group_from_file(students_file)
# Parse given files, create instances of Student class and create instances of Group class (title for group is name of json-file without extension).

import json
from json import JSONEncoder

class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    @classmethod
    def from_json(cls, json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)

        return cls(**data)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    @classmethod
    def serialize_to_json(cls, student, json_file):
        with open(json_file, 'w') as f:
            json.dump(student.__dict__, f)


class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    def __str__(self):
        out_string = f'{self.title}: ["'
        for student in self.students:
            out_string += str(student) + '", "'
        return out_string[0:-3] + ']'

    @classmethod
    def serialize_to_json(cls, list_of_groups, filename):
        with open(filename, 'w') as f:
            json.dump(list_of_groups, f, default=lambda s: s.__dict__)

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file, 'r') as f:
            title = f.name[:-5]
            data = json.load(f)

        students = []
        if isinstance(data, list):
            for item in data:
                students.append(Student.from_dict(item))
        else:
            students = [Student.from_dict(data)]

        return cls(title, students)
