
import pickle,getpass,webbrowser,pyautogui,time
j=getpass.getuser()
with open("mode.txt", "rb" ) as mymode:
    a2 = pickle.load(mymode)
with open("path.txt", "rb" ) as mypath:
    path1 = pickle.load(mypath)
path1=path1.replace("/","\\")
g="C:\\Users\\username\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
g=g.replace('username',j)
if a2==1:
    webbrowser.open(g)
    time.sleep(1)
    pyautogui.typewrite('cd "'+path1+'"')
    pyautogui.press('Enter')
    time.sleep(1)
    pyautogui.typewrite('start easy.pyw')
    pyautogui.press('Enter')
    time.sleep(1)
    pyautogui.typewrite('exit')
    pyautogui.press('Enter')
if a2==2:
    webbrowser.open(g)
    time.sleep(1)
    pyautogui.typewrite('cd "'+path1+'"')
    pyautogui.press('Enter')
    time.sleep(1)
    pyautogui.typewrite('start mediam.pyw')
    pyautogui.press('Enter')
    time.sleep(1)
    pyautogui.typewrite('exit')
    pyautogui.press('Enter')
if a2==3:
    webbrowser.open(g)
    time.sleep(1)
    pyautogui.typewrite('cd "'+path1+'"')
    pyautogui.press('Enter')
    time.sleep(1)
    pyautogui.typewrite("start hard.pyw")
    pyautogui.press('Enter')
    time.sleep(1)
    pyautogui.typewrite('exit')
    pyautogui.press('Enter')