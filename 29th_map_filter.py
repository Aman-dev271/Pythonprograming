# numners = ["2","34","56"]
# for i in range(len(numners)):
#     numners[i] = int(numners[i])
#     print(type(numners[i]))
# numners[2] = numners[2]+28
# print(numners[2])
# by map function 

# numners = ["2","34","56"]
# # for i in range(len(numners)):
# #     numners[i] = int(numners[i])
# #     print(type(numners[i]))
# numners = list(map(int, numners))
# numners[2] = numners[2]+28
# print(type(numners[2]))

# another method to use the map function
# def sq(a):
#     return a*a
# numbers = ["1","2",'3',"4","5"]
# num = list(map(int, numbers))
# print(num, type(num[1]))
# number = list(map(sq, num))
# print(number)


# by lambda function
numbers = ["1","6",'3',"4","5"]
num = list(map(int, numbers))
print(num, type(num[1]))
num1 = list(map(lambda a: a**a , num))
print(num1)



# map function
def squre(a):
    return a*a
def cube(a):
    return a*a*a
fun = [squre , cube]
for i in range(10):
    sqcube = list(map(lambda a: a(i),fun))
    print(sqcube)