# in the python we learn about if else try exception to handle theerrors in the python
# so today we learn about the Else with try Exception and A 'finally'statement in python


# finally is executed all the time if error occure or not and it is written in the end of the try exception

#and else part can be written before the finally  the  else part only executed when the except part does not work
f = open("aman.text")
print(f)
try:
    f1 = open("aman2.txt")
    print(f1)
except EOFError as e:
    print("print EOFError in the line",e)
except IOError as e:
    print("print IOError in the line",e)
else:
    print("It works only when except part does not executed execuuted")
finally:
    print("It print always  ")
    f.close()
    print(f)
    f1.close()
    print(f1)
