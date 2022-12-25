class Std:

    _schoolname = "Devops Univ"# class attribute
    __name = "private"
    _color = "red protected"
    def __init__(self,name, age):
        self.__name = name #instance attribute
        self.__age =age

    def _sample(self):
        print(self._schoolname)

class college(Std):
    pass

c = college("Tom", 1)
print(c._schoolname)
print(c._color)
print(c.__name)