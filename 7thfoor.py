# for loop
list = ['amandeep','mandeep','singh']
for item in list:
    print(item)
# list in list
list1 = [['amandeep' ,4],["deep" ,5],["singh"  ,6]]
for item,number in list1:
    print("item is:" ,item +','+"number is:", number)  
# by the dictionary
dict1  = dict(list1)
print(type(dict1))
for key,number in dict1.items():
    print(key , number)
# if i want only key
for item in dict1:
    print(item)
 