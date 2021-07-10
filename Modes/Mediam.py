#Importing Modules
from plyer import notification
from playsound import playsound
import time,pickle,getpass,os,shutil,webbrowser
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

Directory = os.path.dirname(os.path.realpath(__file__)) #to take File path
Directory=Directory.replace(r"\Sub-Main\Modes","")
def pic():
    import time
    salah=Tk()
    salah.title("Come To Success")
    screen_width = salah.winfo_screenwidth()
    screen_height = salah.winfo_screenheight()
    salah.resizable(False,False)
    mycolor = '#d3d3d3'
    salah.configure(background=mycolor)
    salah.attributes("-fullscreen", True)
    salah.wm_attributes("-topmost", 1)
    img2=Image.open("Icon\\pic.png")
    image1 = img2.resize((screen_width, screen_height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image1)
    Label(salah,image=img).pack()
    hour=StringVar()
    minute=StringVar()
    second=StringVar()
    hour.set("00")
    minute.set("15")
    second.set("00")
    def disable_event():
        pass
    salah.protocol("WM_DELETE_WINDOW", disable_event)

    Button(text="Click here to quit",command=salah.destroy,padx=10,pady=10,bg="#f4f5f0", font="defalt 20 bold italic").place(x=150,y=350)
    Label(salah,text="   Its time for Prayer",width=30, font="Arial 20 bold italic").place(x=-10,y=200)
    Label(salah,width=45,text="Please go and Pray dont delay",bg="#f4f5f0", font="Arial 20 bold italic").place(x=-10,y=250)
    hourEntry= Entry(salah, width=2, font="Arial 80",bg="#f4f5f0",textvariable=hour)
    hourEntry.place(x=450,y=300)
    minuteEntry= Entry(salah, width=2, font="Arial 80",bg="#f4f5f0",textvariable=minute)
    minuteEntry.place(x=600,y=300)
    
    secondEntry= Entry(salah, width=2, font="Arial 80",fg="White",bg="#3b2e1e",textvariable=second)
    secondEntry.place(x=750,y=300)

    
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
            
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
        
        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        salah.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            time.sleep(2)
            salah.destroy()
        
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
    salah.mainloop()


dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
username=getpass.getuser()#to take username

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
    playsound(audio_mp3,False)
    notification.notify(title="Its the time for Duhar",
    message='''QURAN 2:110,
"And establish prayer and give zakah, and whatever good you put forward for yourselves 
You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
    app_icon= appicon,
    timeout=120,
    toast=False)
    try:
        pic()
    except Exception as e:
        print(e)
    
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
    try:
        pic()
    except Exception as e:
        print(e)
    
if b==(salahtimes[2]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
    print(b,"Its the time for Asr")
    playsound(audio_mp3,False)
    notification.notify(title="Its the time for Duhar",
    message='''QURAN 2:110,
"And establish prayer and give zakah, and whatever good you put forward for yourselves 
You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
    app_icon= appicon,
    timeout=120,
    toast=False)
    try:
        pic()
    except Exception as e:
        print(e)
    
if b==(salahtimes[3]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
    print(b,"Its the time for Magrib")
    playsound(audio_mp3,False)
    notification.notify(title="Its the time for Duhar",
    message='''QURAN 2:110,
"And establish prayer and give zakah, and whatever good you put forward for yourselves 
You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
    app_icon= appicon,
    timeout=120,
    toast=False)
    try:
        pic()
    except Exception as e:
        print(e)
    
if b==(salahtimes[4]):  #YOU CAN CHANGE ACCORDING TO YOUR PLACES 
    print(b,"Its the time for Isha")
    playsound(audio_mp3,False)
    notification.notify(title="Its the time for Duhar",
    message='''QURAN 2:110,
"And establish prayer and give zakah, and whatever good you put forward for yourselves 
You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
    app_icon= appicon,
    timeout=120,
    toast=False)
    try:
        pic()
    except Exception as e:
        print(e)
        
webbrowser.open(Directory+"\\Sub-Main\\mode_selector.pyw")