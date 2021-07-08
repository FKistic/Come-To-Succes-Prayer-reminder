
from os import name
import pickle,time,webbrowser
from tkinter import *
from PIL import ImageTk,Image
import os
from tkinter import messagebox 
dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
with open("Data\\Directory.dat",'wb') as modes:
    pickle.dump(dir_path,modes)

root = Tk()
p1 = PhotoImage(file = "icon\\bg.png")
root.iconphoto(False,p1)
#Logic
def call():
    import subprocess
    subprocess.call(fr'"{dir_path}\Sub-Main\ChangeSalahTime.pyw"', shell=True)

def logic():
    if mode_value.get()==1:
        mode=1
        with open("Data\\mode.dat",'wb') as modes:
            pickle.dump(mode,modes)
    if mode_value.get()==2:
        mode=2
        with open("Data\\mode.dat",'wb') as modes:
            pickle.dump(mode,modes)
    if mode_value.get()==3:
        mode=3
        with open("Data\\mode.dat",'wb') as modes:
            pickle.dump(mode,modes)
    if mode_value.get()==4:
        mode=4
        with open("Data\\mode.dat",'wb') as modes:
            pickle.dump(mode,modes)
    a="questions",messagebox.askquestion("Submitted", "Confirm?\nDo You want to quit?")
    if a[1]=="yes":
        webbrowser.open(dir_path+"\\Sub-Main\\mode_selector.pyw")
        time.sleep(5)
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

mode_value=IntVar()


#Labels

Label(root,text="Welcome to Come To Success\nPrayer Remainder",bg="#2e3192",foreground="white",font="Defalt 15 bold").place(x=5,y=5)
Label(text='''This program is made to notify you about salah timings''',font="Times 12 italic underline",bg="#2e3192",fg="white").place(x=5,y=70)
Label(text='''Different modes available this programs are:''',font="Times 12 italic underline",bg="#2e3192",fg="white").place(x=5,y=120)
Label(text='''1. Easy mode - ONLY NOTIFICATIONS AND ALERTS.''',font="Times 12 italic underline",bg="#2e3192",fg="white").place(x=40,y=150)
Label(text='''2. Mediam mode - FULL SCREEN NOTIFICATION WITH TIMER With End Button''',font="Times 12 italic underline",bg="#2e3194",fg="white").place(x=40,y=180)
Label(text='''3. Hard mode - FULL SCREEN NOTIFICATION WITH TIMER With NO End Button.''',font="Times 12 italic underline",bg="#2e3194",fg="white").place(x=40,y=210)
Label(text='''4. Extream mode - WILL SHUTDOWN YOUR PC AT AZAN TIME.''',font="Times 12 italic underline",bg="#2e3194",fg="white").place(x=40,y=240)

# CheckBoxes

mode=Radiobutton(bg="#2e3192",variable=mode_value,value=1).place(x=10,y=150)
mode=Radiobutton(bg="#2e3192",variable=mode_value,value=2).place(x=10,y=180)
mode=Radiobutton(bg="#2e3192",variable=mode_value,value=3).place(x=10,y=210)
mode=Radiobutton(bg="#2e3192",variable=mode_value,value=4).place(x=10,y=240)

#Button
Button(text="Submit",command=logic,padx=10,bg="#2e3192",fg="white").place(x=50,y=270)
Button(text="Change Prayer Time",bg="#2e3192",fg="white",command=call,padx=10).place(x=650,y=10)
root.mainloop()
with open("Data\\mode.dat",'rb') as modes:
    a=pickle.load(modes)
    print(a)

    
 

