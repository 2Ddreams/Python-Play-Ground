import random
from typing import ParamSpecArgs

letter_check_display = {1: "", 2: "", 3: "", 4: "", 5: ""}

word_bank = ["apple", "table", "water"]

chosen_word = random.choice(word_bank).upper()

tries = 5


def InterfaceBlock():
    print("-----")
    answer = input("Guess Word: ")
    return answer

def WordMatchingBlock(chosen_word, answer_word):
    for i in range(5):
        print(i)
        if answer_word[i] == chosen_word[i]:
            letter_check_display[i] = "clcp"
        elif i in chosen_word:
            letter_check_display[i] = "wlcp"
        elif i not in chosen_word:
            letter_check_display[i] = "wlwp"
    return letter_check_display
            



answer = InterfaceBlock()
for i in "p":
    pass
while tries <= 0 :
    answer = InterfaceBlock()
    for i in chosen_word:
        for i in "p":
            pass
        
    pass



print(WordMatchingBlock(chosen_word, answer))
print(chosen_word)