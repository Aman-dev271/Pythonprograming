import time
initial = time.time()
print(initial)
i = 2
while i<23:
    print("i am amandeep")
    time.sleep(2)
    i = i+1
print("time take by while loop",time.time() -initial ,"is")

print(time.asctime(time.localtime(time.time())))