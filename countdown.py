import getpass,pyautogui,time,webbrowser,pickle
with open("path.txt", "rb" ) as mypath:
    path1 = pickle.load(mypath)
cmd_path="C:/Users/username/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Command Prompt.lnk"
user=getpass.getuser()
cmd_path=cmd_path.replace("username",user)
def countdown(t): 
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1    
    pyautogui.alert(text='I hope you have prayed?', title='Come To Succes', button='Yess!,i have prayed')
t = 1200
countdown(int(t))
cmd_path="C:/Users/username/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Command Prompt.lnk"
user=getpass.getuser()
cmd_path=cmd_path.replace("username",user)
time.sleep(1)
webbrowser.open(cmd_path)
time.sleep(1)
pyautogui.typewrite('cd "'+path1+'"')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite("start mode_selector.py")
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('exit')
time.sleep(1)
pyautogui.press('enter')