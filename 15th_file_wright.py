#  to make new file by the python
a = open("aman2.txt" , "w")
f =a.write("amandeep ne seekh liya hai k kese new file bn skte hai\n ")
# if i wan to know that char that wewritten  in the file

print(f)
a.close()


# to add some char after the line the or new line
b  = open("aman2.txt" , "a")
g = b.write("i am new line\n")

#  to read write both mode
b  = open("aman2.txt" , "r+")


c = b.write("i can use both\n ")
print(b.read())
