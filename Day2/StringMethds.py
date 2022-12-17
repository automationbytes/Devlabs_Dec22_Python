a = "PYTHON"
print(len(a)) #length of string

#indexing
print(a[0])
#negative indexing
print(a[-4])

#slicing
print(a[2:5])

#negative slicing
print(a[-5:-2])

print(a[2:])

print(a[:5])

print(a[:-3])

#Strip
a = "   hello   world     "
print(a)
print(a.strip())
print(a.lstrip())
print(a.rstrip())

#lower and upper
a = "helloworld"
print(a.upper())
b = "HELLO"
print(b.lower())

c = "dD Fluß"
print(c.lower())
print(c.casefold())

d = "python is popular.java is outdated"
print(d.capitalize())
print(d.title())

e = "India has Multiple lang"
print(e.swapcase())

words=e.split(" ")
print(words)

#replace
print(e.replace("a","aa"))

#concat
a = "apple"
b = "mango"
print(a+b)
c = 5
print(a+str(c))

a = "Apple"
print(a.count("p"))

a = "hello world"
print(a.find("W"))

#print(a.index("W"))

acctnum = "578"
print(acctnum.zfill(16))
