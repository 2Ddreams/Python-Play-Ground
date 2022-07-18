import random

list_of_superpowers = ["you can fly", "you can be invisible"]
list_of_buts = ["You can only use it for 1 minute", "Your clothes can't "]


final_output_superpowers = random.choice(list_of_superpowers)
final_output_buts = random.choice(list_of_buts)

final_output1 = f"Your super power is {final_output_superpowers} but..."
final_output2 = f"{final_output_buts}"

for i in range(2):
    print("----------------------------------------------------------------")
print(final_output1)
input("")
print(final_output2)
for i in range(2):
    print("----------------------------------------------------------------")

