l= 10 #global var
def fucntion(n):
    # l = 5
    global l #it is user to change the global value
    l= 30
    
    print(l,"this is local")
    print(n,"this is printed")
fucntion("thisi snew")
print(l)


def function1():
    global l 
    l = l-10
    print("this is fucntion000")
function1()
print(l)



# nested function
l = 4
def aman():
    x = 30
    def ani():
        global l
        l = l+10
    print("before callingani()",x)
    ani()
    print("after callin ani()" , l)
aman()
print(l)