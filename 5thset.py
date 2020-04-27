list = [1,2,3,4,5,6,7,8,]
list2= [2,3,4,5]
makeset = set(list)
print(type(makeset))
print(makeset)

set = set()
# to add the element into the set
# set does not contain the same item more the one time

set.add(1)
set.add(2)
print(set)
# for union
print(set.union({1,2}))

# intersection 
s = set.intersection({1,2,3,4})
print(s , set)

# for lenght
print(len(s))
print(max(set))

# to check the disjont
print(set.isdisjoint({3,4}))

# for remove the value 
print(set)
# set.remove(1)
print(set)

# indexing
# set does not suporting indexing
# print(set[1])




 