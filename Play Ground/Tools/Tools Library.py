import random

#Text Spacer
def TextSpacer(lines):
    if lines == "blank":
        print(" ")
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
