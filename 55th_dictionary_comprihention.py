# if i want a dictionary as output like:-{o:Item0,1:"Item1".............}
# so we have two methods to do this
# first method is :-
dictionary = {}
for i in range(1, 100):
    if i%5==0:
        dict1 = {i:f"Item{i}"}
        print(dict1)
# secon method is by use of dictionary comprihension
dict1 = {i:f"Item{i}" for i in range(100) if i%2==0 }
# print(dict1)


# to reverse the dictionry in the order like {Item0:0,Item1:"1".............}
dict1 = {i:f"Item{i}" for i in range(30) if i%2==0 }
dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n", dict2)
