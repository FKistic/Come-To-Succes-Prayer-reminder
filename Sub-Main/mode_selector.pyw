import pickle,getpass,webbrowser,time,os,shutil,subprocess
from datetime import datetime
j=getpass.getuser()
dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
dir_path1=str(dir_path)
dir_path1=dir_path1.replace("\\Sub-Main",'')
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
            print("File already present)")
        except Exception as e:
            print(e)


dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
file_path=dir_path+r"\mode_selector.lnk"
startup_path=r"C:\Users\use\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
startup_path=startup_path.replace("use",j)
finder(file_path,startup_path)
a2=int(a2)
print(a2)
with open(f"{dir_path1}\\Data\\SalahTimes.dat",'rb') as salahtime:
    salahtimes=pickle.load(salahtime)
salahtimes=str(salahtimes)
salahtimes=salahtimes.replace("[","")
salahtimes=salahtimes.replace("]","")
salahtimes=salahtimes.replace("'","")
salahtimes=salahtimes.split(",")
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
with open(f"{dir_path1}\\Data\\TimeNow.dat",'wb') as time1:
    pickle.dump(b,time1)

if a2==1:
    webbrowser.open(fr'{dir_path1}\Modes\Easy.py')
if a2==2:
    webbrowser.open(fr'{dir_path1}\odes\Mediam.py')
if a2==3:
    webbrowser.open(fr'{dir_path1}\Modes\Hard.py')
if a2==4:
    webbrowser.open(fr'{dir_path1}\Modes\Extream.py')