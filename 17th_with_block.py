# if we dont want to close the file by the close() then we ave short hand method
with open("aman.text") as a:
    f =a.readline()
    f =a.readlines()
    print(f)
a = open("aman.text" , "rt")
print(a.readline())
