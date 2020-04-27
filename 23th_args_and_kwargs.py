# in smple function
def name(a,b,c,d):
    print(a,b,c,d)
name("amadeep","singh","mani","pooja")



#  args and kwargs functions
def dunxtionargs(*args):
    print(type(args))
    print(name)
name = ["aman","amandeep","amandeep singh","katnoria"]
dunxtionargs(*name)

# for loop
def dunxtionargs(normal, *args):
    print(normal)
    print(type(args))
    for i in args:
        print(i)
name = ["aman","amandeep","amandeep singh","katnoria"]
second = "i am noral arguments"
dunxtionargs(second,*name)


# kewargs
def function(normal , *args ,**kewargs):
    print(normal)
    for i in args:
        print(i)
    print("\nintroduced to our heroess")
    for key, values in kewargs.items():
        print(f"{key} is a {values}")
normal = "i am normal "
name = ["amandeep","singh","katnoria","singh"]
dictkwargs = {"aman":"programmer","deep":"bisinessman","amandeep":"programmer plus business man and billonear"}
function(normal , *name , **dictkwargs)