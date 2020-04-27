# List comprehension in python
# write a program to print the number that are divisible by 3
ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)
print(ls)
# To do this in one line we use the List comprehensions
# let see
ls = [ i for i in range(100) if i%10 == 0 ]
print(ls)
