KEY = "usRmNILUjyizDcQpeJEXMCHPSk"

alphabet = "abcdefghijklmnopqrstuvwxyz"

code_dict = {}

encrypted_word = ""

counter = 0

#for i in word:
#    current_word = word.index(i)
#print(current_word)

word = input("Word To Encrypt: ")

#print(len(alphabet))
for i in range(len(alphabet)):
    code_dict[alphabet[counter]] = KEY[counter]
    counter += 1
    #print(counter)

#print(code_dict)

for i in word:
    encrypted_word += str(code_dict.get(i))
print(encrypted_word)
