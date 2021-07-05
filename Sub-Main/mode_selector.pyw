
import pickle,getpass,webbrowser,time,os,shutil
j=getpass.getuser()
with open("Data\\mode.dat", "rb" ) as mymode:
    a2 = pickle.load(mymode)
def remove(names):
    names=names.split(",")
    a=len(names)
    index=0
    while index<a:
        try:
            b=os.remove(fr"C:\Users\use\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\{names[index]}")
            index+=1
        except Exception as e:
            print(e)
            index+=1

a2=str(a2)
a2=a2.replace("[","")
a2=a2.replace("]","")
a2=int(a2)
print(a2)
dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
if a2==1:
    webbrowser.open(dir_path+"\\Modes\\Easy.pyw")
    startup_path=r"C:\Users\use\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    startup_path=startup_path.replace("use",j)
    shutil.copy(dir_path+"\\Easy.pyw",startup_path)
    remove("Mediam.pyw,Hard.pyw,Extream.pyw")
    
if a2==2:
    webbrowser.open(dir_path+"\\Modes\\Mediam.pyw")
    startup_path=r"C:\Users\use\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    startup_path=startup_path.replace("use",j)
    shutil.copy(dir_path+"\\Modes\\Mediam.pyw",startup_path)
    remove("Easy.pyw,Hard.pyw,Extream.pyw")
if a2==3:
    webbrowser.open(dir_path+"\\Modes\\Hard.pyw")
    startup_path=r"C:\Users\use\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    startup_path=startup_path.replace("use",j)
    shutil.copy(dir_path+"\\Modes\\Hard.pyw",startup_path)
    remove("Mediam.pyw,Easy.pyw,Extream.pyw")
if a2==4:
    webbrowser.open(dir_path+"\\Modes\\Extream.pyw")
    startup_path=r"C:\Users\use\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    startup_path=startup_path.replace("use",j)
    shutil.copy(dir_path+"\\Modes\\Extream.pyw",startup_path)
    remove("Mediam.pyw,Hard.pyw,Easy.pyw")