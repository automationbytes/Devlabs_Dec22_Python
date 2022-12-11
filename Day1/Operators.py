'''
Operators - its a symbolic notations used to perform some operations on variables/values

Arithmetic operators
Comparison operators
Assignment operators
Bitwise operators
Logical operators
Membership operators
Identity operators


'''
a = 10
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #mod modulo modulus -> remainder
print(a//b) #floor division -> quotient
print(a**b) # exponential /power of

#comparison - comparing 2 values / true or false
a = 4
b = 6
print(a == b) #equals
print(a != b) #not equals
print(a < b) #less than
print(a > b) #greater than
print(a <= b) #lesser than or equal to
print(a >= b) #greater than or equal to

#Assignment - assign the values back to the variables
a = 5
#a = a + 5
a += 5 # a = a+5
print(a)



#logical operators
'''
and
true and true = true
true and false = false
false and true = false
false and false = false

or
true or true = true
true or false = true
false or true = true
false or false = false

not
true -> false
false -> true
'''

a = 4
b = 1
c = 8
# print(a<b)
# print(a<c)
print(a < b and a < c)
print(a < b or a < c)
print(a<c)
print(not(a<c))


#Bitwise operators
'''
& - binary and
| - binary or
~ - binary not (negotion)
'''

a = 14 #-> 1110
b = 3 #->  0011
         # 0011

print(a & b)
print(a | b)
'''
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0

'''


#membership operator

str = ["python","java","c++","r"]
print("qr" not in str)

#identity operator

#is
#is not

a = 'india'
b = "india"
print(a)
print(b)