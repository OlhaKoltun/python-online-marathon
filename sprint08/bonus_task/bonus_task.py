import json
import re
from enum import Enum
import uuid


class Role(Enum):
    Mentor = 1
    Trainee = 2


class Score(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'


class NonUniqueException(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f'User with name {self.username} already exists'


class PasswordValidationException(Exception):
    def __str__(self):
        return 'Invalid password'


class ForbiddenException(Exception):
    def __str__(self):
        return 'Forbidden'


class Subject:
    def __init__(self, title, subject_id=str(uuid.uuid4().hex)):
        self.id = subject_id
        self.title = title

    def __str__(self):
        return self.title


class Grade:
    def __init__(self, user_id, subject_id, title, score):
        self.user_id = user_id
        self.subject_id = subject_id
        self.title = title
        self.score = score

    def __repr__(self):
        return str({self.title: self.score.name})


class User:
    def __init__(self, user_id, username, password, role):
        self.id = user_id
        self.username = username
        self.password = password
        self.role = role
        self.grades = []

    def __str__(self):
        return f'{self.username} with role {self.role}: {self.grades}'

    @staticmethod
    def create_user(username, password, role):
        password_pattern = '(?=.*[0-9])(?=.*[!@#$%^&*_])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*_]{6,}'

        if re.match(password_pattern, password):
            user_id = uuid.uuid4()
            return User(user_id, username, password, role)
        else:
            raise PasswordValidationException()

    def add_score_for_subject(self, subject, score):
        self.grades.append({str(subject): str(score.name)})

    def user_to_dict(self):
        return {'id': str(self.id),
                'username': self.username,
                'password': self.password,
                'role': str(self.role)}


def get_subjects_from_json(subjects_json):
    with open(subjects_json, 'r') as f:
        data = json.load(f)

    subjects = [Subject(item['title'], item['id']) for item in data]

    return subjects


def get_users_with_grades(users_json, subjects_json, grades_json):
    with open(users_json, 'r') as users_file:
        users_data = json.load(users_file)

    users = [User(item['id'], item['username'], item['password'], item['role']) for item in users_data]

    subjects = get_subjects_from_json(subjects_json)

    with open(grades_json, 'r') as grades_file:
        grades = json.load(grades_file)

    for grade in grades:
        subject = None
        for subj in subjects:
            if grade['subject_id'] == subj.id:
                subject = subj.title
        for user in users:
            if grade['user_id'] == user.id:
                user.grades.append({subject: grade['score']})

    return users


def add_user(user, users):
    if user.username in [item.username for item in users]:
        raise NonUniqueException(user.username)

    users.append(user)


def check_if_user_present(username, password, users):
    for user in users:
        if user.username == username and user.password == password:
            return True

    return False


def add_subject(subject, subjects):
    if subject.title in [item.title for item in subjects]:
        raise NonUniqueException(subject.title)

    subjects.append(subject)


def get_id_by_title(title, subjects):
    for subject in subjects:
        if subject.title == title:
            return subject.id

    return None


def get_grades_for_user(username: str, user: User, users: list):
    grades = None
    if user.role == Role.Mentor or username == user.username:
        for user in users:
            if user.username == username:
                grades = user.grades
    else:
        raise ForbiddenException()

    return grades


def users_to_json(users, json_file):
    with open(json_file, 'w') as users_file:
        json.dump([user.user_to_dict() for user in users], users_file)


def subjects_to_json(subjects, json_file):
    with open(json_file, 'w') as subjects_file:
        json.dump([subject.__dict__ for subject in subjects], subjects_file)


def grades_to_json(users, subjects, json_file):
    grades = []
    for user in users:
        for grade in user.grades:
            grades.append({'user_id': str(user.id),
                           'subject_id': str(get_id_by_title(list(grade.keys())[0], subjects)),
                           'score': list(grade.values())[0]})
    with open(json_file, 'w') as grades_file:
        json.dump(grades, grades_file)


def file_contains(json_file, arg, value):
    with open(json_file, 'r') as file:
        data = json.load(file)
    if any([len(item[arg]) != value for item in data]):
        return True

    return False