import random
import ToolsLibrary as tl

letter_check_display = {0: "", 1: "", 2: "", 3: "", 4: ""}
letter_check = {0: "", 1: "", 2: "", 3: "", 4: ""}



word_bank = tl.TextToListConverter("WordBank - Wordle.txt")

chosen_word = random.choice(word_bank)

tries = 5


#Text Spacer
def TextSpacer(lines):
    if lines == "blank":
        print(" ")
    else: 
        for i in range(lines):
            print("----------------------------------------------------------------")


def InterfaceBlock():
    TextSpacer(2)
    answer = input("Guess Word: ")
    return answer.lower()

def WordMatchingBlock(chosen_word, answer_word):
    for i in range(5):
        if answer_word[i] == chosen_word[i]:
            letter_check_display[i] = "GREEN"        #"cpcl" Correct Place Correct Letter
            letter_check[i] = True
        elif answer_word[i] in chosen_word:
            letter_check_display[i] = "YELLOW"       #"wpcl" Wrong Place Correct Letter
            letter_check[i] = False
        elif answer_word[i] not in chosen_word:
            letter_check_display[i] = "RED"          #"wpwl" Wrong Place Wrong Letter
            letter_check[i] = False

    return letter_check_display, letter_check
            


def ListToDisplayFormat(list_var):
    final_display = ""
    counter = 0
    for i in list_var:
        counter += 1
        final_display += f"[ {counter}: {i} ] "
    return final_display


    

TextSpacer(5)
answer = InterfaceBlock()
tries -= 1

# Chosen Word
# print(chosen_word)
TextSpacer(1)
print(ListToDisplayFormat(tl.DictToListConverter(WordMatchingBlock(chosen_word, answer)[0])))
check_list = tl.DictToListConverter(WordMatchingBlock(chosen_word, answer)[1])
#print(check_list)
#print(f"Tried: {tries}")
if answer != chosen_word:
    print(f"Tries Left: [ {tries} ]")
else:
    pass



while tries >= -1 or all(check_list) != True:
    check_list = tl.DictToListConverter(WordMatchingBlock(chosen_word, answer)[1])
    if all(check_list):
        #print(all(letter_check))
        break
    else:
        answer = InterfaceBlock()
        tries -= 1
        TextSpacer(1)
        # print(chosen_word)
        print(ListToDisplayFormat(tl.DictToListConverter(WordMatchingBlock(chosen_word, answer)[0])))
        if tries == -1:
            print(f"Tries Left: [ NONE ] - Press Enter To See Word.")
        elif tries == 0:
            print(f"Tries Left: [ LAST TRY ] - Next Try Won't Be Counted.")
            
        else:
            print(f"Tries Left: [ {tries} ]")

        if tries == -1:
            break


if all(check_list):
    TextSpacer(2)
    print(f"Well Done You Got The Word In ( {5 - tries} ) Tries")
    TextSpacer(2)
else:
    TextSpacer(2)
    print("You Ran Out Of Tries")
    print(f"The Word Was: {chosen_word.upper()}")
    TextSpacer(2)


