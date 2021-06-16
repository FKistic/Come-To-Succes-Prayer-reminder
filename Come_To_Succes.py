import pickle,pyautogui,time,webbrowser
import getpass
USER_NAME = getpass.getuser()
print("Come to Salah, Come to succes")
print("This program is made by Faraaz Kurawle")
print('''This program is made to notify you about salah timings
Different modes in this programs are:
1. Easy mode - ONLY NOTIFICATIONS AND ALERTS.
2. Mediam mode - FULL SCREEN NOTIFICATION WITH TIMER
3. Hard mode - This mode will remind you 5 mins before the azan time to let yousave all your work, AND WILL SHUT DOWN THE COMPUTER AT AZAN TIME!.
NOTE:- use 1,2,3 only!''')
mode= int(input("Which mode you want to chose: "))
with open("mode.txt", "wb" ) as mymode:
    pickle.dump(mode, mymode)
path=input("Please Enter the path where you have extracted this programs: ")
path=path.replace("\\","/")
with open("path.txt", "wb" ) as mypath:
    pickle.dump(path, mypath)
with open("path.txt", "rb" ) as mypath:
    path1 = pickle.load(mypath)
if input('Have opened this program for the first time?(y/n)?: ')=='y':
    print("Oh,ok so now this program make it self to run at start up")
    file_path="C:\\Users\\user\\Documents\\Python\\Come_To_Succes\\startup!"
    start_path="C:\\Users\\use\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    start_path=start_path.replace('use',USER_NAME)
    file_path=file_path.replace('user',USER_NAME)
    webbrowser.open(file_path)
    time.sleep(1)
    pyautogui.hotkey('ctrl','a')
    time.sleep(1)
    pyautogui.hotkey('ctrl','x')
    time.sleep(1)
    pyautogui.hotkey('ctrl','w')
    time.sleep(1)
    webbrowser.open(start_path)
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    pyautogui.hotkey('ctrl','w')
from subprocess import call
call(["python",path1+"/mode_selector.py"])
