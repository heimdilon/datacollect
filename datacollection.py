# Created by kor_a at 24/07/2021
import os
import pyautogui
import time

directory = os.getcwd()


for i in range(1000):
    im = pyautogui.screenshot(region=(315, 310, 1270, 715))         //take screenshots of spesific area
    im.save(r'{}\{}.jpg'.format(directory, i))      //save screenshots to current working directory
    time.sleep(5)     //wait 5 second
