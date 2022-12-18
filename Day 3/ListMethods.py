vegetables = ["carrot","potato","tomato","cabbage","onion"]
print(vegetables)
#update
vegetables[2] = "Red Tomato"
print(vegetables)

#adding
#append - end of list
vegetables.append("beans")
print(vegetables)

#insert - insert values in specified index
vegetables.insert(3,"pumpkin")
print(vegetables)

#extend
fruits = ["Apple","Mango","Banana","Apple","Grapes"]
fruits.extend(vegetables)
print(fruits)

#copy - clone
newveg = vegetables.copy()
print(newveg)
vegetables.append("onion")
print(vegetables)
print(newveg)
print("*************")
veg = vegetables
print(veg)
vegetables.append("onion")
print(vegetables)
print(veg)


#remove
vegetables.remove("onion")
print(vegetables)

#pop with index - remove spefied index
vegetables.pop(6)
print(vegetables)

#pop without index - remove last value
vegetables.pop()
print(vegetables)

#clear - remove all the values from list
vegetables.clear()
print(vegetables)
#
# #del - deletes the complete list from memory
# del vegetables
# print(vegetables)

vegetables = ['carrot', 'potato', 'Red Tomato', 'pumpkin', 'cabbage', 'onion', 'beans', 'onion', 'onion']
#count - get the number of occurenences
print(vegetables.count("onion"))

#index - provides the index of particular value
print(vegetables.index('pumpkin'))

#index for invalid value - it will throw an error
#print(vegetables.index("apple"))

#sorting
vegetables.sort()
print(vegetables)

#sorting with descending order
vegetables.sort(reverse=True)
print(vegetables)



vegetables = ['carrot', 'potato', 'Red Tomato', 'pumpkin', 'cabbage', 'onion']

#reversing
vegetables.reverse()
print(vegetables)


