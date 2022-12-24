fruits = {"Apple","Mango","Banana","Stawberry","Apple","Banana","Banana"}
print(fruits)

#add - can be added in any position
fruits.add("Grapes")
print(fruits)

#update - add two sets
newfruits = {"Blueberry","Orange","Stawberry"}
fruits.update(newfruits)
print(fruits)

#remove
fruits.remove("Blueberry")
print(fruits)
#pop - it will remove any random value
print(len(fruits))
fruits.pop()
print(fruits)
print(len(fruits))

#discard - discard will not throw any error if values are not thr
fruits.discard("Mango")
print(fruits)

#clear
newfruits = fruits.copy()
print(newfruits)
newfruits.clear()
print(newfruits)

fruits = {"Grapes","Apple","Orange","Banana"}
company = {"Apple","Orange","Google","Microsoft"}

print(fruits.intersection(company))
# fruits.intersection_update(company)
# print(fruits)

#sym diff
print(fruits.symmetric_difference(company))
#sym diff update willupdate existing result
#union
print(fruits.union(company))
#update
print(fruits.difference(company))

#superset -  returns true, if all the values of set 2 present in set 1
x = {1,7,8,9}
y = {1,9}
print(x.issuperset(y))
print(y.issubset(x))