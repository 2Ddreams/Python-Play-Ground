import random
import time

inventory = {"hp_flask" : 1}
health = 100
attack = 1
attack_speed = 1


events = ["Spawn Mobs (0)"]
cave_mobs = ["Zombie"]

def InventoryChecker():
    for item, amount in inventory.items():
        print(f"{item} : {amount}")
    input("")
    return "Inventory Closed"

def TextSpacer(num_of_spaces):
    for i in range(num_of_spaces):
        print("-----------------------------------------------------------------------")

def MobGenerator(mob_list, mob_health_min, mob_health_max, mob_attack_min, mob_attack_max, mob_attack_speed_min, mob_attack_speed_max):
    mob_type = random.choice(mob_list)
    mob_health = random.randrange(mob_health_min, mob_health_max)
    mob_attack = random.randrange(mob_attack_min, mob_attack_max)
    mob_attack_speed = random.randrange(mob_attack_min, mob_attack_max)
    return mob_type, mob_health, mob_attack, mob_attack_speed


def DealDamage(self_hp, self_atk, target_hp, target_atk, self_atk_spd, target_atk_spd):
    for i in range(self_atk_spd):
        target_hp -= self_atk
    for i in range(target_atk_spd):
        self_hp -= target_atk
    return target_hp, self_hp


def MobFocus(mob_type1, mob_hp1, mob_atk1, mob_atk_spd1):
    mob_type = mob_type1
    mob_hp = mob_hp1
    mob_atk = mob_atk1
    mob_atk_spd = mob_atk_spd1
    return mob_type, mob_hp, mob_atk, mob_atk_spd


def AttackSequence(player_hp, player_atk, mob_hp, mob_atk, self_atk_spd, mob_atk_spd):
    f_hp = DealDamage(player_hp, player_atk, mob_hp, mob_atk, self_atk_spd, mob_atk_spd)
    health - f_hp[1]
    mob_hp -= f_hp[0]
    
    





def EventGenerator():
    num_of_events = len(events)
    choice_of_event = random.randrange(0, num_of_events)
    if choice_of_event == 0:
        mob_gen = MobGenerator(cave_mobs, 1, 10, 1, 5, 1, 3)
        print(f"You Encountered a {mob_gen[0]}") 
        print(f"Health : {mob_gen[1]}")
        print(f"Attack : {mob_gen[2]}")
        print(f"Attack Speed : {mob_gen[3]}")
        TextSpacer(1)
        print("Do You Wish To Engage The Fight.")
        TextSpacer(1)
        ActionBlock(mob_gen[1], mob_gen[2], mob_gen[3])


    else:
        print("Nothing Happened.")

def StatusChecker():
    print("Your Stats:")
    print(f"Health: {health}")
    print(f"Attack: {attack}")
    print(f"Attack Speed: {attack_speed}")




def ActionBlock(mob_hp, mob_atk, mob_atk_spd):
    TextSpacer(1)
    print("Type (esc) at any time to save and quit the game.")
    print("Attack / Retreat / Inventory (a/r/i)")
    TextSpacer(2)
    StatusChecker()
    TextSpacer(1)    

    action = input("Input: ")
    TextSpacer(1)
    if action.lower() == "a":
        AttackSequence(health, attack, mob_hp, mob_atk, attack_speed, mob_atk_spd )
        input("")
        return "Attack"
    elif action.lower() == "r":
        input("")
        return "Retreat"
    elif action.lower() == "i":
        InventoryChecker()
        return "Inventory"
    elif action.lower() == "esc":
        with open("ProgressSave.txt", "w") as f:
            f.writelines(str(health))
            f.write(":")
            f.writelines(str(attack))
        with open("Inventory.txt", "w") as f:
            if inventory != "":
                f.writelines(str(inventory))
        time.sleep(1)
        print("SAVED!")
        quit()
    else:
        print("That is not a valid move.")
        input("")
        


# GAME STARTS HERE
TextSpacer(5)
print("Welcome to the experimental Games.")
print("Would you like to start a NEW GAME or LOAD from save. (n/l)")
load_or_cont = input("")
if load_or_cont == "n" or load_or_cont == "l":
    start_game = True
else:
    print("Invalid Input")
    start_game = False

while start_game == False:
    TextSpacer(5)
    print("Welcome to the experimental Games.")
    print("Would you like to start a NEW GAME or LOAD from save. (n/l)")
    load_or_cont = input("")
    if load_or_cont == "n" or load_or_cont == "l":
        start_game = True
    else:
        print("Invalid Input")
        start_game = False


if load_or_cont.lower() == "n":
    print("Welcome to the Mythtic Land!")
    while health > 0:
            TextSpacer(5)
            EventGenerator()
    
elif load_or_cont.lower() == "l":
    with open("ProgressSave.txt", "r") as f:
        stats_dict = {}
        for i in f:
            health, attack = i.strip().split(":")
            stats_dict[health] = attack
            print(stats_dict)
    try: 

        with open("Inventory.txt", "r") as f:
            for i in f: 
                item, amount = i.strip().split(":")
                inventory[item] = amount
                print(inventory)
    except ValueError:
        print("Inventory is empty")
    #print("Welcome to the Mythtic Land!")
    #while health > 0:
            #TextSpacer(5)
            #EventGenerator()
    print("Load Function Not Complete Yet")







