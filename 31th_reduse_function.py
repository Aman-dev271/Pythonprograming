list  =[1,2,3,4,5,6,7,8]
num= 0
for i in list:
    # print(i)
    num = num+i
    # print(num ,end=" ")
print(num)

# reduce function
from functools import reduce
num1 =reduce(lambda a,b:a+b, list)

print(num1)