import os

os.system("cls")

counter  = 0


def TextSpacer(line_type=None, lines=1):
    if line_type == "blank":
        print(" ")
    elif line_type == "=":
        for i in range(lines):
            print("================================================================")
    else: 
        for i in range(lines):
            print("----------------------------------------------------------------")
    


plus_or_minus = input("ADD (+) / MINUS (-): ")
while plus_or_minus != "":
    if plus_or_minus == "+":
        counter += 1;
        TextSpacer("=")
        print(f"[COUNTER VALUE]: [{counter}]")
        TextSpacer("=")
    elif plus_or_minus == "-":
        counter -= 1;
        TextSpacer("=")
        print(f"[COUNTER VALUE]: [{counter}]")
        TextSpacer("=")
    else:
        TextSpacer("=")
        print(f"[INVALID INPUT]")
        TextSpacer("=")
    plus_or_minus = input("ADD (+) / MINUS (-): ")


TextSpacer("=")
print(f"END - Final Value: [{counter}]")
TextSpacer("=")