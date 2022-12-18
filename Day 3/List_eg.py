'''

List can store in sequential order (insertion order)
List can allow duplicates
List can allow modification (mutable)
[]
homogeneous  and  hetro data (same and diff)
Elements based on index

'''

fruits = ["Apple","Mango","Banana","Apple","Grapes"]
print(fruits)


#constructors
names = list(["tom","jerry","scooby","jack","jill"])
print(names)
print(type(names))

#length of the list
print(len(fruits))

#indexing (starts from 0)
print(fruits[2])

#negative indexing (starts from last value -1)
print(fruits[-4])

#Slicing - Cutting down the list into smaller list
#['Apple', 'Mango', 'Banana', 'Apple', 'Grapes']

print(fruits[1:4])

#negative slicing
print(fruits[-4:-1])

print(fruits[2:])
print(fruits[:4])
print(fruits[-4:])
print(fruits[:-2])

print(fruits[:])
#['Apple', 'Mango', 'Banana', 'Apple', 'Grapes']
print(fruits[1:5:2]) #start, stop, step

print(fruits[slice(1,5,2)])
print(fruits[slice(1,5)])

#Loops
vegetables = ["carrot","potato","tomato","cabbage","onion"]
print(vegetables)

for i in range(0,len(vegetables),1):
    print(vegetables[i])

print("*****************************")

for i in range(len(vegetables)):
    print(vegetables[i])
print("*****************************")
#for each - extended for

for a in vegetables:
    print(a)

name = "vignesh"
for n in name:
    print(n)
    if "e" in n:
        print("available")
        break

i = 0
while i < len(vegetables):
    print(vegetables[i])
    i = i+1


mlist = [1,"abc",7.5,True]
print(mlist)

#shorthand for
#vegetables = ["carrot","potato","tomato","cabbage","onion"]
[print(i) for i in vegetables]

#shorthand for iwit if
newveg = [i for i in vegetables if i!="tomato"]
print(newveg)

[print(i) for i in vegetables if i!="tomato"]

for i in vegetables:
    if i!="tomato":
        print(i)

[print(i) if i!="tomato" else "potato" for i in vegetables]