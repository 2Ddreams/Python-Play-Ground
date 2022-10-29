import os

L_KEY = "usRmNILUjyizDcQpeJEXMCHPSk"
S_KEY = ""
N_KEY = ""


alphabet = "abcdefghijklmnopqrstuvwxyz"

numbers = "1234567890"

symbols = "!@#$%^&*():;'<>?,./\|`~"

code_dict = {}

decrypted_word = ""

counter = 0


with open("file2.txt", "r") as f:
    text = f.read()


for i in range(len(alphabet)):
    code_dict[L_KEY[counter]] = alphabet[counter]
    counter += 1

    
for i in text:
    decrypted_letter = str(code_dict.get(i))
    if decrypted_letter == "None":
        decrypted_word += " "
    else:
        decrypted_word += str(code_dict.get(i))



print(decrypted_word)

