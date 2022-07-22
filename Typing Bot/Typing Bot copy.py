from pynput.keyboard import Controller
import time
import cv2
import pytesseract
import pyautogui



keyboard = Controller()


lines = int(input(""))

time.sleep(2)

for i in range(lines):
    time.sleep(0.01)
    keyboard.press(str(i))
  






