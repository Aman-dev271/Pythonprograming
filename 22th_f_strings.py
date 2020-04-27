import math
# string formatting
# a = "amandeep"
# b = "this is %s"%a
# print(b)


a = "amandeep"
a1 = 3
b = "this is %s  %s"%(a, a1)
print(b)

# dot format
aman = "amandeep"
a1 = 2
a = "this is  {} {}"
b = a.format(aman, a1)
print(b)


# F-string
me = "mandeep"
a1 = 23344445
a = f"this is {me} {a1} {12*3} {'the valueis', math.cos(45)}"
print(a)