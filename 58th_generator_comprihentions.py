# generator comprihentions
gen = (i for i in range(1, 100) if i%3==0)
# print(gen)
# for i in gen:
#     print(i)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
