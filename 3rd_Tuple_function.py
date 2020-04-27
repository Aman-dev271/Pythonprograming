# in the tuple we can not change the value of the object 
# tuple is immutable nd list is mutable
# if we want no one can change my list value 
tp = (1,2,4)
print(tp)
print(type(tp))


# as i told you we can not set new value in tuple so 
# if we want ot do that 
tp[1] = 56#it can't change because tuple is immutable
print(type(tp))

tp = (1,2,4)
# tupple for one value
tp1 = (1,)
print(tp1)
# tupple for zero value 
tp_for_zero = tuple()
# to know the type of that 
print(type(tp_for_zero))