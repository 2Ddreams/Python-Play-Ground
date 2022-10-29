import random
import os
import time


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
    
#Random Number Generator
def RandomNumGen(start, stop):
    num = random.randrange(start,stop+1)
    return num

# Combines Two Lists into One Dictionary
def ListToDictionaryCombinator(key_list, item_list ):
    dictionary = {}
    for i in range(len(key_list)):
        dictionary[key_list[i]] = item_list[i]
    return dictionary

def DictToListConverter(dictionary): 
    check_list = []
    for i in range(len(dictionary)):
        check_list.append(dictionary.get(i))
    return check_list

def Square(num_to_square):
    answer = num_to_square * num_to_square
    return answer

def Multiplicator(num1, num2):
    ans = num1 * num2
    return ans

def Adder(num1, num2):
    ans = num1 + num2
    return ans

def Divider(num1, num2):
    ans = num1 / num2
    return ans

def Differenciator(num1, num2):
    ans = num1 - num2
    return ans

def StringCounter(string):
    counter = 0
    for i in range(len(string)):
        counter += 1
    return counter

def TextToListConverter(text_file):
    return_list = []
    with open(text_file, "r") as f:
        for i in f.readlines():
            return_list.append(i.strip())
    return return_list

def Absolute(num):
    if num < 0:
        return num * -1
    else:
        return num

def ClearScreen():
    os.system("cls")