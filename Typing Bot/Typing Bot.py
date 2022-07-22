from pynput.keyboard import Controller
import time
import cv2
import pytesseract
import pyautogui



keyboard = Controller()


pyautogui.alert("3 Seconds Left!!")
time.sleep(3)

pyautogui.screenshot("screenshot.png")


list_of_words = "Everyone is afraid of something. We fear things because we value them. We fear losing people because we love them. We fear dying because we value being alive. Don't wish you didn't fear anything. All that would mean is that you didn't feel anything."
for i in list_of_words:
    time.sleep(0.01)
    keyboard.press(i)







