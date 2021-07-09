#Importing Modules
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

with open(f"{Directory}\\Modes\\TimeNow.dat") as timenow1:
    b=pickle.load(timenow1)
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
    
webbrowser.open(Directory+"\\Sub-Main\\mode_selector.pyw")
