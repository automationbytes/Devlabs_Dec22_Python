i = 100
while i<=10:
    print("hello", i)
    i = i+1

#reverse a number
num = 5791 # 1975
reversenum = 0

while num > 0:
    remainder = num % 10 # 5  # 7
    reversenum = reversenum * 10 + remainder #0*10 + 5=> 5*10 + 7 -57
    num = num // 10 #197

print(reversenum)
print(type(reversenum))


num1 = 5791 # 1975
numstr = str(num1)
print(numstr[::-1]) #reverse
print(type(numstr))

str = "hello world"
print(str[::-1])