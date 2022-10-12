# Your task is to write a program which allows teachers to create a multiple choice test in a class called Testpaper
# and to be also able to assign a minimum pass mark. The testpaper's subject should also be included. The attributes are in the following order:
# 1. subject
# 2. markscheme
# 3. pass_mark
# As well as that, we need to create student objects to take the test itself! Create another class called Student and do the following:
# Create an attribute called tests_taken and set the default as  'No tests taken'.
# Make a method called take_test(), which takes in the testpaper object they are completing and the student's answers. 
# Compare what they wrote to the mark scheme, and append to the/create a dictionary assigned to tests_taken in the way as shown in the point below.
# Each key in the dictionary should be the testpaper subject and each value should be a string in the format seen in the examples below 
# (whether or not the student has failed, and their percentage in brackets).

class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark

    def get_pass_mark(self):
        return int(self.pass_mark[:self.pass_mark.index('%')])


class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, test_paper, answers):
        correct_answers = sum([1 for item in answers if item in test_paper.markscheme])
        
        mark = round(correct_answers / len(answers) * 100)
        
        if type(self.tests_taken) == str:
            self.tests_taken = dict()

        if mark >= test_paper.get_pass_mark():
            self.tests_taken[test_paper.subject] = f'Passed! ({mark}%)'
        else:
            self.tests_taken[test_paper.subject] = f'Failed! ({mark}%)'
