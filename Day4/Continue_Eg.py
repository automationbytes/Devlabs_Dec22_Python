if 5 < 18:
    pass

mylist = [[1], [2,3],[4,5]]
flatlist = []

for sublist in mylist:
    print(sublist)
    for s in sublist:
        flatlist.append(s)

print(flatlist)