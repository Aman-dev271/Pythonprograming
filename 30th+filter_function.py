price =  [2000,120,200000,200,3000,300,30,10,40]
def greator_th_100_and_less_th_1000(num):
    return num>100 and num<1000

print(list(filter(greator_th_100_and_less_th_1000 , price)))