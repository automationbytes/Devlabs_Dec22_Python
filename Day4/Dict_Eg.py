'''
Dict - use key and value pair
key - will not allow duplicates
value - can allow duplicates

3.7 - ordered 3.6 - unordered
{}

'''

mydic = {
    "fruit" :"Apple",
    "vegetable": "Carrot",
    "language":"python",
    "vegetable":"onion"
}

print(mydic)
print(len(mydic))

#accessing elements
print(mydic["vegetable"])
print(mydic.get("vegetable"))

#print all keys
print(mydic.keys())

#print all values
print(mydic.values())

#print both
print(mydic.items())

#ffor loop

#keys
for k in mydic.keys():
    print(k)

#values
for v in mydic.values():
    print(v)

#items
for k,v in mydic.items():
    print(k," - ",v)
