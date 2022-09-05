import random
import os

alphabet = "abcdefghijklmnopqrstuvwxyz"
cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

split_alphabet_list = []
split_cap_alphabet_list = []

counter = 0

for i in range(len(alphabet)):
    split_alphabet_list.append(alphabet[counter])
    split_cap_alphabet_list.append(cap_alphabet[counter])
    counter += 1

print(split_cap_alphabet_list)
print(split_alphabet_list)