# The cache means to store the tempraroy page that we need so many times
# for example if we search ay site over the chrome browser so chrome save that page into the memory of the hardware and this is called cache
import time
from functools import lru_cache
@lru_cache(maxsize=3)
def addition(n1, n2):
    time.sleep(3)
    number = n1+n2
    print(f"the additon answer is {number}")
if __name__ == '__main__':
    print("function start")
    time.sleep(3)
    addition(2, 19)
    print("calling .......")
    time.sleep(3)
    print("second_done.........")
