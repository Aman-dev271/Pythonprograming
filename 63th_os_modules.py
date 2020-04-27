import os
# print(os.getcwd())
# f= open("aman.text","r")
# print(f.read())
# print(os.listdir("c://"))
# to chnage directory
# os.chdir("c://")
# print(os.getcwd())
# to make a dir
# os.mkdir("this")
# to make two directory
# os.makedirs("aman/mandeep")
# os.chdir("g://pythontut/aman")
# os.mkdir("aman2")
# os.chdir("g://pythontut/aman/aman2")
# os.mkdir("aman.py")
# print(os.listdir())
# to rename the file naem
# os.rename("aman.text","mannii.text")


# to the path software
print(os.environ.get('path'))

# to add the or join the path
print(os.path.join("c:/","/aman.text"))


# to know the path is exist or not
print(os.path.exists("c://program"))


# to check it is directory or a file
print(os.path.isdir("c://"))
# to know it is file or diectory
print(os.path.isfile("mannii.text"))
