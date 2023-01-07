'''
try - test the block of code with error/might contains error
except - when we hav an error in try, it will come to except block and execute the code inside
finally - irrespective of the try/except results it will be executed. Mainly used for clean up activities
else - optional -
'''
import traceback

try:
    print(a)

except:
    print("An exception occured")
    traceback.print_exc()
print("hello")

try:
    print(10/0)
except ZeroDivisionError:
    print("ZeroDivisionError has occured")
    traceback.print_exc()
except NameError:
    print("Name error has occured")

try:
    print(abc)
except:
    print("hello")
finally:
    print("finally")


#else will be executed only when try part is executed
try:
    print("abc")
except:
    print("hello")
else:
    print("else")

#raise - used to create user defined exceptions

age = 5
if age < 18:
    raise Exception("Sorry Not Eligible")