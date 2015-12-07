# coding:utf-8
__author__ = 'uv2sun'


class Student(object):
    count = 0
    books = []

    def __init__(self, name, age):
        print(self)
        self.name = name
        self.age = age

    @classmethod
    def say(cls):
        print(cls)



Student.books.extend(['book1', 'book2'])
Student.books.append('book3')
print('student book list:%s' % Student.books)

Student.hobbies = ['reading', 'fucking']
print('student hobby list:%s' % Student.hobbies)
print(dir(Student))

s = Student('litx', 22)
s.say()
