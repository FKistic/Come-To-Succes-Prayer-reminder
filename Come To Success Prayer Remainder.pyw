
from os import name
import pickle,time,webbrowser
from tkinter import *
from PIL import ImageTk,Image
import os
from tkinter import messagebox 
dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
with open("Data\\Directory.dat",'wb') as modes:
    pickle.dump(dir_path,modes)
root1 = Tk()
root1.title("Come To Success")
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()
root1.geometry('300x50')
root1.resizable(False,False)
mycolor = "#2e3192"
img2=ImageTk.PhotoImage(Image.open("icon\\bg.png"))
p1 = PhotoImage(file = "icon\\bg.png")
root1.iconphoto(False,p1)
root1.configure(background=mycolor)
Label(root1,text='Please Select only one CheckBox and Click Submit',background="#2e3192",foreground="white").pack()
Button(root1,text="Click here!",background="#2e3192",foreground="white",command=root1.destroy).pack()
root1.mainloop()


root = Tk()
p1 = PhotoImage(file = "icon\\bg.png")
root.iconphoto(False,p1)
#Logic
def call():
    import subprocess
    subprocess.call(fr'"{dir_path}\Sub-Main\ChangeSalahTime.pyw"', shell=True)

def logic():
    if mode1_value.get()==True:
        mode=1
        l1=[]
        l1.append(mode)
        l2=list(set(l1))
        with open("Data\\mode.dat",'wb') as modes:
            pickle.dump(l2,modes)
    if mode2_value.get()==True:
        mode=2
        l1=[]
        l1.append(mode)
        l2=list(set(l1))
        with open("Data\\mode.dat",'wb') as modes:
            pickle.dump(l2,modes)
    if mode3_value.get()==True:
        mode=3
        l1=[]
        l1.append(mode)
        l2=list(set(l1))
        with open("Data\\mode.dat",'wb') as modes:
            pickle.dump(l2,modes)
    if mode4_value.get()==True:
        mode=4
        l1=[]
        l1.append(mode)
        l2=list(set(l1))
        with open("Data\\mode.dat",'wb') as modes:
            pickle.dump(l2,modes)
    a="questions",messagebox.askquestion("Submitted", "Confirm?\nDo You want to quit?")
    if a[1]=="yes":
        webbrowser.open(dir_path+"\\Sub-Main\\mode_selector.pyw")
        root.destroy()

        
# Main windows Configs
root.title("Come To Success")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('800x600')
root.resizable(False,False)
mycolor = '#d3d3d3'

root.configure(background=mycolor)

#BG Images

img2=ImageTk.PhotoImage(Image.open("icon\\bg.png"))
Label(root,image=img2).pack()

#Values

mode1_value=BooleanVar()
mode2_value=BooleanVar()
mode3_value=BooleanVar()
mode4_value=BooleanVar()

#Labels

Label(root,text="Welcome to Come To Success\nPrayer Remainder",bg="#2e3192",foreground="white",font="Defalt 15 bold").place(x=5,y=5)
Label(text='''This program is made to notify you about salah timings''',font="Times 12 italic underline",bg="#2e3192",fg="white").place(x=5,y=70)
Label(text='''Different modes available this programs are:''',font="Times 12 italic underline",bg="#2e3192",fg="white").place(x=5,y=120)
Label(text='''1. Easy mode - ONLY NOTIFICATIONS AND ALERTS.''',font="Times 12 italic underline",bg="#2e3192",fg="white").place(x=40,y=150)
Label(text='''2. Mediam mode - FULL SCREEN NOTIFICATION WITH TIMER With End Button''',font="Times 12 italic underline",bg="#2e3194",fg="white").place(x=40,y=180)
Label(text='''3. Hard mode - FULL SCREEN NOTIFICATION WITH TIMER With NO End Button.''',font="Times 12 italic underline",bg="#2e3194",fg="white").place(x=40,y=210)
Label(text='''4. Extream mode - WILL SHUTDOWN YOUR PC AT AZAN TIME.''',font="Times 12 italic underline",bg="#2e3194",fg="white").place(x=40,y=240)

# CheckBoxes

mode1=Checkbutton(bg="#2e3192",variable=mode1_value).place(x=10,y=150)
mode2=Checkbutton(bg="#2e3192",variable=mode2_value).place(x=10,y=180)
mode3=Checkbutton(bg="#2e3192",variable=mode3_value).place(x=10,y=210)
mode3=Checkbutton(bg="#2e3192",variable=mode4_value).place(x=10,y=240)

#Button
Button(text="Submit",command=logic,padx=10,bg="#2e3192",fg="white").place(x=50,y=270)
Button(text="Change Prayer Time",bg="#2e3192",fg="white",command=call,padx=10).place(x=650,y=10)
root.mainloop()


    
 

