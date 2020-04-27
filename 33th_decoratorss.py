"""
def function():
    print("subscribe now Tech Aman")



fun1 = function
del function
fun1()



def fun_returner(num):
    if num== 0:
        return print
    if num == 1:
        return sum
a = fun_returner(0)
print(a)



# function as an argument we also can use
def fun_as_argument(aman):
    aman("amandeep is a good boy and this function is take a function as an argument")
fun_as_argument(print)


"""


# decorator function
def dec_function(func1):
    def now_execute():
        print("The Execution start")
        func1(a1,b2)
        print("The Execution Is Done")
    return now_execute
# this is another way to define the decorator
# @dec_function
def aman_ka_function(a1, b2):
    c= a1+b2
    print(f"addition answer of {a1} and {b2} is ={c}")
    

a1 = int(input("Enter the value of 'a'"))
b2 = int(input("Enter the value of 'b' "))
# actual work decorator
aman_ka_function = dec_function(aman_ka_function)
aman_ka_function()
