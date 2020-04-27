# in python have
# Itrateable = .__iter__()  or .__getitem__
# Itrate = .__next__()
# Itration = to itrate again and again


# generator work as like range fucntion
for i in range(100):
    print(i)
# in these loop it does not store the value it genrate in fly and display


#in the generter we will store the items into the generator and itrate it by these methods
# in python have
# Itrateable = .__iter__()  or .__getitem__
# Itrate = .__next__()
# Itration = to itrate again and again
def gen(n):
    for i in range(n):
        yield (i)
a  =  gen(10)
# print(a.__next__())
# # ithis is called itration
print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())


h = "amandeep"
# we declare here that h is Itrateable
p = iter(h)
print(p.__next__())
print(p.__next__())
