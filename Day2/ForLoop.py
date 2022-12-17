#start, stop, step

for i in range(1,10,1):
    print(i)

print("--------------------------")


for i in range(1,10,2):
    print(i)


print("--------------------------")

for i in range(10,1,-2):
    print(i)


print("--------------------------")
#start - 0 and step 1
for i in range(10):
    print(i)

print("--------------------------")

#step as 1
for i in range(5,10):
    print(i)

print("--------------------------")
for i in range(10,2):
    print(i)
#===================================

for i in range (100):
    print(i)
    if i == 50:
        break
print("**********************")

for i in range(10):
    print(i, "outer")
    for j in range(3):
        print("inner")