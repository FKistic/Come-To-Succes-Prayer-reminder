'''
This Program is meant to help people struggling with praying salah on time.
feel free to edit the code, but pls dont remove this comment and my social media block even if you edit.
May Allah bless You
Author: Faraaz Kurawle
'''
import webbrowser
if input("Do you have PYAUTOGUI module installed(y/n)?: ")=='n':
    print('please follow the instructions!')
    print("type this in powershell 'pip install pyautogui' to install")
    webbrowser.open("https://pypi.org/project/PyAutoGUI/")
    exit()
else:
    print("NICE!")
if input("Do you have PLYER module installed(y/n)?: ")=='n':
    print("type this in powershell 'pip install plyer' to install")
    webbrowser.open("https://pypi.org/project/plyer/")
    exit()
else:
    print("Awesome!")
if input("Do you have PLAYSOUND module installed(y/n)?: ")=='n':
    print("type this in powershell 'pip install playsound' to install")
    webbrowser.open("https://pypi.org/project/playsound/")
    exit()
else:
    print('Fantastic,Please Continue')
#From here starts my Social Media block, please dont remove this too
if input("Do you want follow me on social media(y/n)?: ")=='y':
    print("Follow me on instagram!")
    webbrowser.open("https://www.instagram.com/faraaz_kurawle/")
    print("My StackOverFlow profile!")
    webbrowser.open("https://stackoverflow.com/users/16187613/faraaz-kurawle?tab=profile")
    print("My Github!")
    webbrowser.open("https://github.com/new/project")
#Social Media block ends here
from subprocess import call
call(["python","Come_To_Succes.py"])