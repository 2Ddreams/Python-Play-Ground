list_of_ice_cream = ["vanilla (v) : 10", "strawberry (s) : 12", "chocolate (c) : 11", "banana (b) : 9"]
dict_of_ice_cream = {"v" : 10, "s" : 12, "c" : 11, "b" : 9}
name_of_ice_cream = {"v" : "vanilla", "s" : "strawberry", "c" : "chocolate", "b" : "banana"}

#Text Spacer
def TextSpacer(lines):
    if lines == "blank":
        print(" ")
    else: 
        for i in range(lines):
            print("----------------------------------------------------------------")
    
TextSpacer(2)
print("Hi, Xiao Ming")
print("Would you like to buy an Ice-cream? (y/n):")
TextSpacer(1)
answer = input("Answer: ")
answer = answer.lower()
if answer == "y":
    TextSpacer(1)
    print("What typ of ice-cream would you like:")
    for i in list_of_ice_cream:
        print(f" - {i}")
    TextSpacer(1)
    type_of_ice_cream = input("Answer: ")
    type_of_ice_cream = type_of_ice_cream.lower()
    TextSpacer(1)
    if type_of_ice_cream in dict_of_ice_cream:
        print(f"That would be ${dict_of_ice_cream.get(type_of_ice_cream)} please.")
        money_given = float(input("How much do you have: "))
        TextSpacer(1)
        if money_given >= dict_of_ice_cream.get(type_of_ice_cream):
            final_amount = money_given - dict_of_ice_cream.get(type_of_ice_cream)
            print(f"Here's your {name_of_ice_cream.get(type_of_ice_cream)} ice-cream")
            print(f"Here's your change of ${final_amount}")
        else:
            print("Sorry, you don't have enough money.")
            print("Come Next Time!")
        TextSpacer(1)
        
    else:
        print("Sorry your choice are not in the options.")
        TextSpacer(1)

        
elif answer == "n":
    TextSpacer(1)
    print("Come next time!")
    TextSpacer(1)

else: 
    TextSpacer(1)
    print("That is not a valid answer.")
    TextSpacer(1)
