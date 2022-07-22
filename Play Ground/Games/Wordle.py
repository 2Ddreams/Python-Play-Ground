import random

letter_check_display = {0: "", 1: "", 2: "", 3: "", 4: ""}

word_bank = ["apple", "table", "water"]

check_list = []

chosen_word = random.choice(word_bank)

tries = 4

word = False

def InterfaceBlock():
    print("-----")
    answer = input("Guess Word: ")
    return answer

def WordMatchingBlock(chosen_word, answer_word):
    for i in range(5):
        if answer_word[i] == chosen_word[i]:
            letter_check_display[i] = True #cpcl
        elif answer_word[i] in chosen_word:
            letter_check_display[i] = "wpcl"
        elif answer_word[i] not in chosen_word:
            letter_check_display[i] = "wpwl"
    return letter_check_display
            
def DictToListConverter(): 
    for i in range(len(letter_check_display)):
        letter_check_display[i] = True
        check_list.append(letter_check_display.get(i))
    


answer = InterfaceBlock()
print(chosen_word)
print(WordMatchingBlock(chosen_word, answer))
DictToListConverter()

while tries != 0:
   
    if all(letter_check_display):
        print(all(letter_check_display))
        exit()
    else:
        answer = InterfaceBlock()
        print(chosen_word)
        print(WordMatchingBlock(chosen_word, answer))
        tries -= 1


if all(letter_check_display):
    print("Well done you completed te puzzle.")
else:
    print("You Ran Out Of Tries")
    print(letter_check_display)


