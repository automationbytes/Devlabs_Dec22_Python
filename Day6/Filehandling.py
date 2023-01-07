'''
read "r"
write "w"
append "a"
create "x"
close
delete


'''

file1 = open("sample.txt","a")
file1.write("Hello world \n")

li = ["apple","orange","banana"]
file1.writelines(li)
file1.close()


with open("witsample.txt","w") as file2:
    file2.write("Hello \n")