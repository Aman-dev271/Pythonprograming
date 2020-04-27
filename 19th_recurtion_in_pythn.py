# # factorial program
# # n! = n * n-1 * n-2 * n-3 ...........1
# # ?n! = n*(n-1)!
def  factorial_itrative(n):
    """
    :param: integre
    # return : n * n-1 * n-2 *n-3 ....1 """
    fac = 1
    for i in range(n):
        fac =fac * (i+1)
    return fac

number = int(input("Eneter the number that you want to solve"))

print(factorial_itrative(number))
a =int(input("Enter 1 for run again and 2 for stop it"))
number = int(input("Eneter the number that you want to solve"))

while a == 1:

    print(factorial_itrative(number))


# recursive function  
def factorial_recursive(n):
    if n == 1:
        return 1
    else :
        return n* factorial_recursive(n-1)
        # 5* factorial_recursive(5-1)
        # 5* 4*factorial_recursive(4-1)
        # 5* *4*3factorial_recursive(3-1)
        # 5**4*3* factorial_recursive(2-1)
        # 5*4*3*2*1
number = int(input("enter the bumber \n"))
print(factorial_recursive(number))




 