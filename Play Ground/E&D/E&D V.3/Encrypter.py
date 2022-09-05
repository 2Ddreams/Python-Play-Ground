import os

KEY = "usRmNILUjyizDcQpeJEXMCHPSk"


alphabet = "abcdefghijklmnopqrstuvwxyz"

numbers = "1234567890"

symbols = "!@#$%^&*():;'<>?,./\|`~"

code_dict = {}

encrypted_word = ""
encrypted_list = []
counter = 0


with open("file.txt", "r") as f:
    text = f.read().lower()


for i in range(len(alphabet)):
    code_dict[alphabet[counter]] = KEY[counter]
    counter += 1

for i in text:
    if i == " ":
        encrypted_word += " "
    else:
        encrypted_word += str(code_dict.get(i))
print(encrypted_word)


for i in text:
    if i == " ":
        encrypted_word += " "
    else:
        encrypted_list.append(str(code_dict.get(i)))
print(encrypted_list)



#with open("file2.txt", "w") as f:
    #f.write(encrypted_word)
    
with open("file2.txt", "w") as f:
    f.write(encrypted_list)
