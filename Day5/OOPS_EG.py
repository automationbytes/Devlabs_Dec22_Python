'''

Student
	#attributes
	name
	age

	#methods
	study
	write
	play

'''
name = "tim"
class Student:
    name = "Tom"
    age = 10

    def study(self):
        print(self.name)

s = Student()
s.study()

class stdnt:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object is deleted")

    def study(self):
        print(self.name)

s1 = stdnt("Tom", 10)
s2 = stdnt("Jack", 12)
s1.study()
s2.study()
del s1
del s2