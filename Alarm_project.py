from pygame import mixer
from datetime import datetime
from time import time
def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def store_msg_with_time(msg):
    with open("masgandtime.txt","a") as aman:
        aman.write(f"{msg}, date and time is {datetime.now()}\n")
if __name__ == '__main__':
    init_water = time()
    init_eye = time()
    init_phy_exersize = time()
    water_take_after = 15
    eyes_excersize_after = 30
    do_phy_excersize_after = 60
    while True:
        if time()- init_water > water_take_after:
            print("paani pio bhai ji and alarm ko stop karne k liye space dba k enter dbao")
            init_water = time()
            musicloop("percent.mp3", " ")
            store_msg_with_time("pani piya at")
        if time()- init_eye > eyes_excersize_after:
            print("aankho ki excersize kro bhai ji and alarm ko stop karne k liye 3 dba k enter dbao")
            init_eye = time()
            musicloop("Aaja Ni Aaja.mp3", "3")
            store_msg_with_time("eye excersize ki at")
        if time()- init_phy_exersize > do_phy_excersize_after:
            print("physical excersize kr lo bhai ji and alarm ko stop karne k liye 4 dba k enter dbao")
            init_phy_exersize = time()
            musicloop("phy.mp3", "4")
            store_msg_with_time("physical excersize ki at")
