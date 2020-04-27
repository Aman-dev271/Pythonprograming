# /we can open files for readings by "r"   -default mode
# write mode  bt "w"
# "x" - to make new files
# "a" - add more content to  end of the file
# "t" - textmode -  defailt mode
# "b" - binary mode
# "+" = read and write


print("file writing")
a = open("aman.text")
# here a  i a pointer that point the return value from the opne()
read = a.read()
print(read)
# it necessery to close the file
a.close()

'''

# the "rb" means it take the file as a binary string
a = open("aman.text" , "rb")
# here a  i a pointer that point the return value from the opne()
read = a.read()
print(read)
# it necessery to close the file
a.close()


# itn that the open () take  "rt" as text mode i.e default mode
a = open("aman.text")
# here a  i a pointer that point the return value from the opne()
# we can also read some char by giving below
read = a.read(3)
print(read)
# it necessery to close the file
a.close()


# we can also read line wise line
f = open("aman.text","rt")
# it generate by default new line operator
for line in f:
    print(line)

f = open("aman.text","rt")

for line in f:
    print(line , end ="")


# we can also read only one line by readline()
d = open("aman.text" , "rt")
print(d.readline())
print(d.readline())



# readlines() to store the lines into alist
b = open("aman.text" , "rt")
print(b.readlines())
''
