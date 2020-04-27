mystr = "aman is  a good boy"
# check length
print(len(mystr))
# indexing
print(mystr[9])
# slicing
print(mystr[0:4])
# slicing
print(mystr[0:30000])
# abvanced slicing
print(mystr[:5])
print(mystr[::])
print(mystr[9:9:3])
# -indexing
print(mystr[-5])
print(mystr[-4:-2])
print(mystr[::-1])
print(type(mystr))
# its output is false because it has space
print(mystr.isalnum())
# its also false
print(mystr.isalpha())
# it checks the ending 
print(mystr.endswith("boy"))
# count the o latter  in the mystr
print(mystr.count("o"))
# to capitalize the string first latter
print(mystr.capitalize())
# to find the string in the string
print(mystr.find("aman"))
# to lower caser
print(mystr.lower())
# to upper case
print(mystr.upper())
# to replace the string
print(mystr.replace("aman","MANDEEP"))


