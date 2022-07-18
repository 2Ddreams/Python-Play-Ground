KEY = "usRmNILUjyizDcQpeJEXMCHPSk"

alphabet = "abcdefghijklmnopqrstuvwxyz"

code_dict = {}

decrypted_word = ""

counter = 0


word = input("Word To Decrypt: ")

for i in range(len(alphabet)):
    code_dict[KEY[counter]] = alphabet[counter]
    counter += 1

    
for i in word:
    decrypted_word += str(code_dict.get(i))
print(decrypted_word)

