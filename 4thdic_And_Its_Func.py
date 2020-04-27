# dictionary is datastructure it keep key value pair
dict1 =  {"aman":"burgar" ,"mani":"kari"
,"deep":"singh","shubham":
{"r":"magggie","c":"ringtone"}}
print(type(dict1))
print(dict1)
print(dict1["shubham"]["r"])
# to extend the dictionary
dict1["ankit"] = "kalu"
# to delete the element from the dictonary
del dict1["ankit"]
print(dict1)
# dictionary functions
# copy function makes the new copy of dict1
dict2 = (dict1.copy())
del dict2["aman"]
print(dict2)
# to get the value by the key
print(dict2.get("mani"))
# to upadate the dictionary
print(dict2.update({"chamdar":"toffee"}))
print(dict2)
# to access all the keys 
print(dict2.keys())
# to get all items 
print(dict2.items())

# itrate the dictionary
dict1={'a':' amandeep','b':' bad'}
print(dict1)
print(dict1['b'])
for i,k in dict1.items():
    print(i+k)
#  how to sort dict
abb={'a':100,'b':200,'c':300}
print(min(zip(abb.values(),abb.keys())))
print(max(zip(abb.values(),abb.keys())))