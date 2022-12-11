'''
Datatpes- specific which data type the value belongs too

Numbers - int, float , complex
Strings
bool - true/false

List
Tuple
Set
Dict

type - is used to print the type of datatype
isinstance - used to check if an object belongs to particular class or not
(true/false)

'''

a = 10797646581346846
print(a)
print(type(a))

b = 3.1479794654941649779779
print(b)
print(type(b))

c = 1+2j
print(c)
print(type(c))

print(isinstance(b,float))

#typecasting - converting from one to other datatype
q = 10
p = float(q)
print(p)
print(type(p))


x = y = z = 10
print(x)
print(y)
print(z)

x,y,z = 4,5,6
print(x)
print(y)
print(z)