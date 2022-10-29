import random
import os

def Absolute(num):
    if num < 0:
        return num * -1
    else:
        return num

#Text Spacer
def TextSpacer(line_type=None, lines=1):
    if line_type == "blank":
        print(" ")
    elif line_type == "=":
        for i in range(lines):
            print("================================================================")
    else: 
        for i in range(lines):
            print("----------------------------------------------------------------")
    
os.system("cls")

guess_counter = 0

TextSpacer("=")
min_num = int(input("Min Num: "))
TextSpacer()
max_num = int(input("Max Num: "))
TextSpacer("=")
random_num = random.randrange(min_num, max_num)
print(random_num)
TextSpacer("blank")
print("Ok! Your Number Has Been Generated. Take a Guess!")
TextSpacer("blank")


TextSpacer("=")
guess_num = int(input("[Input]: "))
guess_counter += 1
buffer_num = guess_num
print(f"BUFFER NUM: [{buffer_num}]")


if guess_num < random_num+5 or guess_num > max_num+5:
    TextSpacer()
    print("THE SUNNN!!")
elif guess_num < random_num+10 or guess_num > max_num+10:
    TextSpacer()
    print("Hot")
elif guess_num < random_num+15 or guess_num > max_num+15:
    TextSpacer()
    print("warm")
elif guess_num < random_num+20 or guess_num > max_num+20:
    TextSpacer()
    print("cold...")
elif guess_num == random_num:
    TextSpacer("=")
    print(f"The Number Was [{random_num}].")
    TextSpacer()
    print(f"You Got The Number In [{guess_counter}] try.")
    TextSpacer("=")


while guess_num != random_num:
    guess_num = int(input("[Input]: "))
    guess_counter += 1
    if (Absolute(buffer_num) - random_num) > (Absolute(guess_num)- random_num):
        TextSpacer()
        print("Hotter!")
    elif (Absolute(buffer_num) - random_num) < (Absolute(guess_num)- random_num):
        TextSpacer()
        print("Colder...")
    elif guess_num == random_num:
        exit()
    buffer_num = guess_num
    print(f"BUFFER NUM: [{buffer_num}]")


TextSpacer("=")
print(f"The Number Was [{random_num}].")
TextSpacer()
print(f"You Got The Number In [{guess_counter}] try.")
TextSpacer("=")


