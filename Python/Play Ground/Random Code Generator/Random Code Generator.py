import random
import os

os.system("cls")

code = ""

alphebet = "abcdefghijklmnopqrstuvwxyz"

numbers = "1234567890"

symbols = "!@#$%^&*():;'<>?,./\|`~"


def TextSpacer(num_of_lines):
    for i in range(num_of_lines):
        print("----------------------------------------------------------------")

def RandomNumGen(min, max):
    num = random.randrange(min, max)
    return num


def CodeType(selection_value):
    # Only Letters
    if selection_value == 0:
        up_or_low = RandomNumGen(0, 2)
        if up_or_low == 0:
            alphebet_selection = alphebet[RandomNumGen(0, 26)] 
        else:
            alphebet_selection = alphebet[RandomNumGen(0, 26)].upper()
        return alphebet_selection 
    # Only Nmbers
    if selection_value == 1:
        numbers_selection = numbers[RandomNumGen(0,10)]
        return numbers_selection
    # Only Symbols
    if selection_value == 2:
        symbols_selection = symbols[RandomNumGen(0,23)]
        return symbols_selection

def CodeConstructorInt(code_length, start, stop):
    final_code = ""
    for i in range(int(code_length)):
        selection_value = random.randrange(start, stop)
        semi_final_code = CodeType(selection_value)
        final_code += semi_final_code
    return final_code

def CodeConstructorStr(code_length, start, stop):
    final_code = ""
    for i in range(len(code_length)):
        selection_value = random.randrange(start, stop)
        semi_final_code = CodeType(selection_value)
        final_code += semi_final_code
    return final_code



TextSpacer(5)

print("Mode Selection")
TextSpacer(1)
print("Random Code (rc) / Only Numbers (on) / Only Letters (ol) / Only Symbols (os)")
TextSpacer(1)
mode = input("input: ").lower()

if mode == "rc":

    code_length = input("Length of Code / Code Conversion: ")

    if code_length[0] in numbers:
        code+=CodeConstructorInt(code_length, 0, 3)
    else:
        code+=CodeConstructorStr(code_length, 0, 3)
        

elif mode == "on":
    code_length = input("Length of Code / Code Conversion: ")

    if code_length[0] in numbers:
        code+=CodeConstructorInt(code_length, 1, 2)

    else:
        code+=CodeConstructorStr(code_length, 1, 2)
    
elif mode == "ol":
    code_length = input("Length of Code / Code Conversion: ")

    if code_length[0] in numbers:
        code+=CodeConstructorInt(code_length, 0, 1)

    else:
        code+=CodeConstructorStr(code_length, 0, 1)

elif mode =="os":
    code_length = input("Length of Code / Code Conversion: ")

    if code_length[0] in numbers:
        code+=CodeConstructorInt(code_length, 2, 3)

    else:
        code+=CodeConstructorStr(code_length, 2, 3)

TextSpacer(2)

print(code) 

TextSpacer(5)

