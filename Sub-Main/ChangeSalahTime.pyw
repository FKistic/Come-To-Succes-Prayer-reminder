#Salah timing 

#import ing module
import pickle,webbrowser
from tkinter import *
from PIL import ImageTk,Image
root2=Tk()
root2.title("Come To Success")
screen_width = root2.winfo_screenwidth()
screen_height = root2.winfo_screenheight()
root2.geometry('800x600')
root2.resizable(False,False)
# Setting icon of master window
mycolor = "#2e3192"
root2.configure(background=mycolor)
img2=ImageTk.PhotoImage(Image.open("icon\\bg.png"))
p1 = PhotoImage(file = "icon\\bg.png")
root2.iconphoto(False,p1)
Label(root2,image=img2).pack()

def Submit():
    l1=[f'{Fajr1.get()}:{Fajr2.get()}:{Fajr3.get()},{Duhar1.get()}:{Duhar2.get()}:{Duhar3.get()},{Asr1.get()}:{Asr2.get()}:{Asr3.get()},{Magrib1.get()}:{Magrib2.get()}:{Magrib3.get()},{Isha1.get()}:{Isha2.get()}:{Isha3.get()}']
    with open("Data\\SalahTimes.dat",'wb') as salahtime:
        pickle.dump(l1,salahtime)
    root2.destroy()
Label(root2,text="Change Prayer Time",bg="#2e3192",foreground="white",font="Defalt 25 bold").place(x=250,y=5)
Label(root2,text='''Fajr :''',font="Times 30 italic underline",bg="#2e3192",fg="white").place(x=5,y=100)
Label(root2,text='''Duhar :''',font="Times 30 italic underline",bg="#2e3192",fg="white").place(x=455,y=100)
Label(root2,text='''Asr :''',font="Times 30 italic underline",bg="#463d84",fg="white").place(x=5,y=200)
Label(root2,text='''Magrib :''',font="Times 30 italic underline",bg="#463d84",fg="white").place(x=450,y=200)
Label(root2,text='''Isha :''',font="Times 30 italic underline",bg="#55447b",fg="white").place(x=5,y=300)

Fajr1=StringVar()
Fajr2=StringVar()
Fajr3=StringVar()

Duhar1=StringVar()
Duhar2=StringVar()
Duhar3=StringVar()

Asr1=StringVar()
Asr2=StringVar()
Asr3=StringVar()

Magrib1=StringVar()
Magrib2=StringVar()
Magrib3=StringVar()

Isha1=StringVar()
Isha2=StringVar()
Isha3=StringVar()

hourEntry1= Entry(root2,width=int(2.5), font=("Arial",40,""),
                 textvariable=Fajr1,bg=mycolor,fg="White")
hourEntry1.place(x=120,y=100)
  
minuteEntry1= Entry(root2, width=int(2.5), font=("Arial",40,""),
                   textvariable=Fajr2,bg=mycolor,fg="White")
minuteEntry1.place(x=190,y=100)
  
secondEntry1= Entry(root2, width=int(2.5), font=("Arial",40,""),
                   textvariable=Fajr3,bg=mycolor,fg="White")
secondEntry1.place(x=260,y=100)

hourEntry2= Entry(root2,width=int(2.5), font=("Arial",40,""),
                 textvariable=Duhar1,bg=mycolor,fg="White")
hourEntry2.place(x=600,y=100)
  
minuteEntry2= Entry(root2, width=int(2.5), font=("Arial",40,""),
                   textvariable=Duhar2,bg=mycolor,fg="White")
minuteEntry2.place(x=665,y=100)
  
secondEntry2= Entry(root2, width=int(2.5), font=("Arial",40,""),
                   textvariable=Duhar3,bg=mycolor,fg="White")
secondEntry2.place(x=730,y=100)

hourEntry3= Entry(root2,width=int(2.5), font=("Arial",40,""),
                 textvariable=Asr1,bg=mycolor,fg="White")
hourEntry3.place(x=120,y=200)
  
minuteEntry3= Entry(root2, width=int(2.5), font=("Arial",40,""),
                   textvariable=Asr2,bg=mycolor,fg="White")
minuteEntry3.place(x=190,y=200)
  
secondEntry3= Entry(root2, width=int(2.5), font=("Arial",40,""),
                   textvariable=Asr3,bg=mycolor,fg="White")
secondEntry3.place(x=260,y=200)

hourEntry4= Entry(root2,width=int(2.5), font=("Arial",40,""),
                 textvariable=Magrib1,bg=mycolor,fg="White")
hourEntry4.place(x=600,y=200)
  
minuteEntry4= Entry(root2, width=int(2.5), font=("Arial",40,""),
                   textvariable=Magrib2,bg=mycolor,fg="White")
minuteEntry4.place(x=665,y=200)
  
secondEntry4= Entry(root2, width=int(2.5), font=("Arial",40,""),
                   textvariable=Magrib3,bg=mycolor,fg="White")
secondEntry4.place(x=730,y=200)

hourEntry5= Entry(root2,width=int(2.5), font=("Arial",40,""),
                 textvariable=Isha1,bg=mycolor,fg="White")
hourEntry5.place(x=120,y=300)
  
minuteEntry5= Entry(root2, width=int(2.5), font=("Arial",40,""),
                   textvariable=Isha2,bg=mycolor,fg="White")
minuteEntry5.place(x=190,y=300)
  
secondEntry5= Entry(root2, width=int(2.5), font=("Arial",40,""),
                   textvariable=Isha3,bg=mycolor,fg="White")
secondEntry5.place(x=260,y=300)

Fajr1.set("04")
Fajr2.set("40")
Fajr3.set("00")

Duhar1.set("12")
Duhar2.set("40")
Duhar3.set("00")

Asr1.set("17")
Asr2.set("16")
Asr3.set("00")

Magrib1.set("19")
Magrib2.set("17")
Magrib3.set("00")

Isha1.set("20")
Isha2.set("40")
Isha3.set("00")
Button(text="Submit",bg="#463d84",fg="white",padx=30,pady=20,command=Submit).place(x=450,y=280)
root2.mainloop()
with open("Data\\SalahTimes.dat",'rb') as salahtime:
    a= pickle.load(salahtime)
a=str(a)
print(int(a))