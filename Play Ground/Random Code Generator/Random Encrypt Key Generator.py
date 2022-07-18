
import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

split_alphabet_list = []
split_cap_alphabet_list = []

final_string = ""

counter = 0


def TextSpacer(lines):
    for i in range(lines):
        print("----------------------------------------------------------------")


for i in range(len(alphabet)):
    split_alphabet_list.append(alphabet[counter])
    split_cap_alphabet_list.append(cap_alphabet[counter])
    counter += 1

for i in range(26):
    decider_value = random.randrange(0, 2)
    if decider_value == 0:
        chosen_lower_letter = random.choice(split_alphabet_list)
        final_string += str(chosen_lower_letter)
        split_alphabet_list.remove(chosen_lower_letter)
    else:
        chosen_upper_letter = random.choice(split_cap_alphabet_list)
        final_string += str(chosen_upper_letter)
        split_cap_alphabet_list.remove(chosen_upper_letter)



print(split_alphabet_list)
print(split_cap_alphabet_list)
TextSpacer(2)
for i in range(len(final_string)):
    final_string.strip("")

print(final_string)