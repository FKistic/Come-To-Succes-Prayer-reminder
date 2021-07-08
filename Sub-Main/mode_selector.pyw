
import pickle,getpass,webbrowser,time,os,shutil,subprocess
j=getpass.getuser()
dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
dir_path1=str(dir_path)
dir_path1=dir_path1.replace("\\Sub-Main",'')
with open(f"{dir_path1}\\Data\\Directory.dat", "rb" ) as myamode:
    a1 = pickle.load(myamode)
with open(f"{dir_path1}\\Data\\mode.dat", "rb" ) as mymode:
    a2 = pickle.load(mymode)
def finder(filepath,startpath):
    a=os.listdir(startpath)
    a=list(a)
    b=0

    index=0
    for i in a:
        if "mode_selector.lnk" in a[index]:
            b+=1
        index+=1
    if b==0:
        try:
            shutil.copy(file_path,startup_path)    
            print("D)")
        except Exception as e:
            print(e)
a=fr'"{dir_path}\Sub-Main\\Mode\\Easy.pyw"'

dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
file_path=dir_path+r"\mode_selector.lnk"
startup_path=r"C:\Users\use\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
startup_path=startup_path.replace("use",j)
finder(file_path,startup_path)
a2=int(a2)
print(a2)
if a2==1:
    webbrowser.open(fr'{dir_path}\Modes\Easy.pyw')

if a2==2:
    webbrowser.open(fr'{dir_path}\odes\Mediam.pyw')
if a2==3:
    webbrowser.open(fr'{dir_path}\Modes\Hard.pyw')
if a2==4:
    webbrowser.open(fr'{dir_path}\Modes\Extream.pyw')