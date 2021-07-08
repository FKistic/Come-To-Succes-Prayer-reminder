#Importing Modules
from datetime import datetime
from plyer import notification
from playsound import playsound
import time,pickle,getpass,os,shutil,webbrowser
from tkinter import messagebox
dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
username=getpass.getuser()#to take username
Directory = os.path.dirname(os.path.realpath(__file__)) #to take File path
Directory=Directory.replace(r"\Sub-Main\Modes","")
#Reading Salah time
with open(f"{Directory}\\Data\\SalahTimes.dat",'rb') as salahtime:
    salahtimes=pickle.load(salahtime)
salahtimes=str(salahtimes)
salahtimes=salahtimes.replace("[","")
salahtimes=salahtimes.replace("]","")
salahtimes=salahtimes.replace("'","")
salahtimes=salahtimes.split(",")

#Files load
fajr_audio=Directory+"\\Audio\\fajr.mp3"
audio_mp3=Directory+"\\Audio\\azan.mp3"
appicon=Directory+"\\Icon\\icon.ico"

while True:#Time Monitor
    time= datetime.now()
    b = time.strftime("%H:%M:%S")
    print(b, end='\r')
    if b==(salahtimes[0]):
        print()
        break
    if b==(salahtimes[1]):
        break
    if b==(salahtimes[2]):
        break
    if b==(salahtimes[3]):
        break
    if b==(salahtimes[4]):
        break
while True:
    if b==(salahtimes[0]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
        print(b,"Its the time for Fajr")
        playsound(fajr_audio,False)#uses playsound moldule
        notification.notify(title="Its the time for Fajr",#uses plyer module
        
        message='''QURAN 2:110,
    "And establish prayer and give zakah, and whatever good you put forward for yourselves 
    You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
        app_icon= appicon,
        timeout=120,
        toast=False)
        break
    if b==(salahtimes[1]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
        print(b,"Its the time for Duhar")
        playsound(audio_mp3,False)
        notification.notify(title="Its the time for Duhar",
        message='''QURAN 2:110,
    "And establish prayer and give zakah, and whatever good you put forward for yourselves 
    You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
        app_icon= appicon,
        timeout=120,
        toast=False)
        break
    if b==(salahtimes[2]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
        print(b,"Its the time for Asr")
        playsound(audio_mp3,False)
        notification.notify(title="Its the time for Asr",
        message='''QURAN 2:110,
    "And establish prayer and give zakah, and whatever good you put forward for yourselves 
    You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
        app_icon= appicon,
        timeout=120,
        toast=False)
        break
    if b==(salahtimes[3]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
        print(b,"Its the time for Magrib")
        playsound(audio_mp3,False)
        notification.notify(title="Its the time for Magrib",
        message='''QURAN 2:110,
    "And establish prayer and give zakah, and whatever good you put forward for yourselves 
    You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
        app_icon= appicon,
        timeout=120,
        toast=False)
        break
    if b==(salahtimes[4]):  #YOU CAN CHANGE ACCORDING TO YOUR PLACES 
        print(b,"Its the time for Isha")
        playsound(audio_mp3,False)
        notification.notify(title="Its the time for Isha",
        app_name="Come to Succes",
        message='''QURAN 2:110,
    "And establish prayer and give zakah, and whatever good you put forward for yourselves 
    You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
        app_icon= appicon,
        timeout=120,
        toast=False)
        break
webbrowser.open(Directory+"\\Sub-Main\\mode_selector.pyw")
