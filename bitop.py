a = 20 #10100 in binary
b = 10#01010
c = a&b
print(c)#00000
c = a|b#11110
print(c)
# rightshift
c=a>>1#01010
print(c)
c= a>>1#01010 in right shift the value will become half
c=a>>2#01010
print(c)
# c= a>>2


# left shift
c= a<<1# 101000 in left bit the value will become double
print(c)
c = a<<2#1010000
print(c)
