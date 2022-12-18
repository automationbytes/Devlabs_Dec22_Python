'''
Tuple - ordered
and not mutable (unchangable)
duplicates are allowed
() - without brackets
multiple datatypes (homo and hetro)

to protect the values (eg payroll- where we will not add/remove/update the values)
'''

#with brackets
names = ("tom","jerry","scooby","jack","jill")
print(names)
print(type(names))

#without brackets
names = "tom","jerry","scooby","jack","jill"
print(names)
print(type(names))

#constructors
names = tuple(("tom","jerry","scooby","jack","jill","tom"))
print(names)
print(type(names))

#indexing
print(names[0])
print(names[-4])
#slicing
print(names[1:3])

print(names.count("tom"))

#index - returns the position the value
print(names.index("jack"))


#for loop
for n in names:
    print(n)

#add/remove/update
names = ("tom","jerry","scooby","jack","jill")
nlist = list(names)
nlist.append("tim")
names = tuple(nlist)
print(names)
print(type(names))



'''
List                                    Tuple
Mutable                             Immutable
slower                              faster
more memory                         less memory
insert,delete,update(write)         read only
[]                                  ()




'''