import json
data = '{"var1":"aman","var2":"deep", "var3":"singh"}'
print(data)
p = json.loads(data)

print(p)
# by this we parsed the data


data1 = {
    "name" : "amandeep",
    "school" :["hatli", "hathlaun"],
    "fridge" : ('icecream', 234),
    "isbad" : False
}
# now it right as python way what we wan to convert it into the java script format so to do that we nee json.dumpd()
c = json.dumps(data1)
print(c)


# Assignment shoet,key parameter in dumps
# what is json.load()
