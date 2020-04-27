# lamda function or anonymous fucntions
def add(a,b):
    return a+b
# and lamda function is written as 
add = lambda a, b: a+b
print(add(2,2))
# lamda is just to make quckly a function or can say it is an shorthand method to make function
 



#  simple fucntion with sorting
def a_first(a):
    return a[1]

a = [[1,12],[2,23],[10,1],[3,0]]
a.sort(key= a_first)
print(a)
#with lamda function sort the list
a = [[1,12],[2,23],[10,1],[3,0]]
a.sort(key= lambda a: a[0])
print(a)