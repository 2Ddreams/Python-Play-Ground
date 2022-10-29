from tkinter import *
from pynput import *
import pyautogui
import os


def on_click(x, y, button, pressed):
    if pressed :
      print("Hi")


with mouse.Listener(on_click=on_click) as Listener:
         Listener.join()
#
#root = Tk()
#
#root.geometry("700x700")
#
#
#
#mainloop()