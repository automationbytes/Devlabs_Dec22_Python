'''
Functions (methods- block of code which will be executed only when its called
parametering
reusability

def funcname(anyparameters):
    return statement


'''


def sum(x,y):
    print(x, "x")
    print(y, "y")
    return x+y

print(sum(10,5))
print(sum(1,25))
print(sum(9,57))

print(sum(y = 5, x = 10))


#tuple
def myfun(*name):
    print(name[1])

myfun("tom","tim","jerry","jack")

#dict
def myfun(**name):
    return (name["last"])

print(myfun(first = "tom", middle = "jack", last= "hendry"))


#default parameter
def dropdown (country = "India"):
    print(country)

dropdown("Aus")

dropdown("US")
dropdown()


c = sum(8,10) *2 / 100
print(c)

def add(a,b):
    return a+b

add = lambda a,b: a+b
print(add(2,3))
