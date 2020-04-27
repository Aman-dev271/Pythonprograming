# Polymorphisum is not an function or any type of builtin module it just an concept that means Ability to take multiple things
# for example
print(4+6)
print("4" + "6")
# this is called pollymorphisum that means to show multiple type in multiple situations like above
# here in both cases be have numbers but n first expression it gives 10 and next it works as string concatination


# to print a 1234....in piramid shape
num = int(input("Enter theRow \n"))
for i in range(1, num+1):
    for j in range(1, num-i+1):
        print(end=" ")
    for j in range(i, 0, -1):
        print(j,end="")
    for j in range(2, i+1):
        print(j,end="")

    print()

# for star in the piramin shape
row_num = int(input("Enter the number of Row's that you want\n"))
for i in range(1, row_num+1):
    for j in range(1,i+1):
        print("#",end=" ")
    print()

# star pattren in opposite to the above
num_Row = int(input("Enter the number of Rows \n"))
for i in range(1, num_Row+1):
    for j in range(1, num_Row-i+1):
        print(end= " ")
    for j in range(i, 0, -1):
        print(j,end="")
    print()
