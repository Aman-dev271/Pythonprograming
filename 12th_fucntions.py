# user define function
# def funname ():
#     print()
def  sum ():
    """This function is to some the two numbers"""
    
    sum = (a+b)
    print(sum)
    return sum
a  = int(input("Enter your number"))
b = int(input("Enter the second number"))
v= sum()
print(v)
print(sum.__doc__)
a  = int(input("Enter your number"))
b = int(input("Enter the second number"))
s= sum()
print(s)

