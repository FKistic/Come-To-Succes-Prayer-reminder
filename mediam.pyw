from datetime import datetime
import time
import pyautogui,webbrowser
from plyer import notification
from PIL import Image
import pickle
import getpass
from playsound import playsound
import os  
a=getpass.getuser()
with open("path.txt", "rb" ) as mypath:
    path1 = pickle.load(mypath)
path_final=path1+"/icon/2.ico"
audio_mp3=path1+"/audio.mp3"
audio_mp3=audio_mp3.replace('user',a)
pic_path=path1+"/icon/pic.jpg"
while True:
    time= datetime.now()
    b = time.strftime("%H:%M:%S")
    print(b, end='\r')
    if b==("04:40:00"):
        break
    if b==("12:40:00"):
        break
    if b==("17:16:00"):
        break
    if b==("19:17:00"):
        break
    if b==("20:40:00"):
        break
while True:
    if b==("04:40:00"):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
        print(b,"Its the time for Fajr")
        playsound(audio_mp3,False)
        webbrowser.open ("C:\\Users\\Faraaz Anas Ammaar\\Documents\\Python\\Come_To_Succes\\icon\\pic.jpg")
        pyautogui.press('f5')
        time.sleep(1)
        notification.notify(title="Its the time for Fajr",
        message='''QURAN 2:110,
"And establish prayer and give zakah, and whatever good you put forward for yourselves 
You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
        app_icon= path_final,
        timeout=20,
        toast=False)
        break
    if b==("12:40:00"):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
        print(b,"Its the time for Duhar")
        playsound("audio.mp3",False)
        webbrowser.open (pic_path)
        pyautogui.press('f5')
        notification.notify(title="Its the time for Duhar",
        message='''QURAN 2:110,
"And establish prayer and give zakah, and whatever good you put forward for yourselves 
You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
        app_icon= path_final,
        timeout=20,
        toast=False)
        break
    if b==("17:16:00"):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
        print(b,"Its the time for Asr")
        playsound(audio_mp3,False)
        webbrowser.open (pic_path)
        pyautogui.press('f5')
        notification.notify(title="Its the time for Asr",
        message='''QURAN 2:110,
"And establish prayer and give zakah, and whatever good you put forward for yourselves 
You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
        app_icon= path_final,
        timeout=20,
        toast=False)
        break
    if b==("19:17:00"):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
        print(b,"Its the time for Magrib")
        playsound(audio_mp3,False)
        webbrowser.open (pic_path)
        pyautogui.press('f5')
        time.sleep(1)
        notification.notify(title="Its the time for Magrib",
        message='''QURAN 2:110,
"And establish prayer and give zakah, and whatever good you put forward for yourselves 
You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
        app_icon= path_final,
        timeout=20,
        toast=False)
        break
    if b==("20:40:00"):  #YOU CAN CHANGE ACCORDING TO YOUR PLACES 
        print(b,"Its the time for Isha")
        playsound(audio_mp3,False)
        webbrowser.open (pic_path)
        pyautogui.press('f5')
        time.sleep(1)
        notification.notify(title="Its the time for Isha",
        app_name="Come to Succes",
        message='''QURAN 2:110,
"And establish prayer and give zakah, and whatever good you put forward for yourselves 
You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
        app_icon= path_final,
        timeout=20,
        toast=False)
        break
from subprocess import call
call(["python", path1+"/countdown.py"])
