import urllib.request
import tkinter.filedialog
from tkinter import *
import pyautogui
import os
import webbrowser

os.system(r"cls")

class OnlineSave:


    def OpenBrowserTab(url):

        urlCheck = isinstance(url, str)
        if urlCheck == True: 
            webbrowser.open_new_tab(url)
        else:
            print("Invalid Input (Has to be a string)")

    def CheckConnection(url="https://www.google.com"):
        webUrl = urllib.request.urlopen(url)
        webUrlCode = webUrl.getcode()

        match webUrlCode:
            case 200:
                print("Stable Connection")
            case 301:
                print("Permanent Redirect")
            case 302:
                print("Temporary Redirect")
            case 404:
                print("Not Found")
            case 410:
                print("Page Gone")
            case 500:
                print("Internal Server Error")
            case 503:
                print("Service Unavailable")
            case _:
                print("Unknown Protocol")


    def urlInput():
        url = pyautogui.prompt("URL HERE")
        openLink = pyautogui.confirm("Open Link Now?")

        if openLink == "OK":
            OnlineSave.OpenBrowserTab(url)
            LocalSave.WriteToOnlineSave(url)
        else:
            LocalSave.WriteToOnlineSave(url)


class LocalSave:
    curDir = os.path.dirname(os.path.abspath(__file__))
    saveLocation = os.path.join(curDir + r"\Saves")
    urlSaveLocation = os.path.join(curDir + r"\Saves\url.save")
    localSaveLocation = os.path.join(curDir + r"\Saves\dir.save")
    
    def WriteToOnlineSave(url):
        with open(LocalSave.urlSaveLocation, "w") as f:
            f.write(url)
        
    def WriteToLocalSave(_dir):
        with open(LocalSave.localSaveLocation, "w") as f:
            f.write(_dir)
        
    def dirInput():


        #_dir = tkinter.filedialog.askdirectory()
        _dir = tkinter.filedialog.askopenfilenames()
        convertedDir = list(_dir)[0]
        #fileNameList = _dir.split("/")
        #fileName = fileNameList[-1]
        #print(_dir)
        #print(str(fileName))
        print(list(_dir)[0])
        openDir = pyautogui.confirm("Open File Now?")
        if openDir == "OK":

            LocalSave.WriteToLocalSave(convertedDir)
        else:
            LocalSave.WriteToLocalSave(convertedDir)




root = Tk()

root.geometry("800x600")


#testButton = Button(text="Online Save", command=lambda:OnlineSave.urlInput())
#testButton.pack()
localSaveButton = Button(text="Local Save", command=lambda:LocalSave.dirInput())
localSaveButton.pack(side=TOP)

onlineSaveButton = Button(text="URL Link", command=lambda:OnlineSave.urlInput())
onlineSaveButton.pack(side=TOP)




mainloop()


