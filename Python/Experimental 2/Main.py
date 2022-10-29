import random
import time

hp = 20
attack = random.randrange(1, 3)

def TextSpacer(num_of_lines):
    for i in range(num_of_lines):
        print("----------------------------------------------------------------")


def MobGen():
    mob_attack = random.randrange(1, 5)
    mob_hp = random.randrange(1, 10)
    return mob_attack, mob_hp

mob_hp = MobGen()[1]
mob_attack = MobGen()[0]

def MobDisplay():
    print(f"Mob Attack: {mob_attack}")
    print(f"Mob Health: {mob_hp}")


def PlayerDisplay():
    print(f"Attack: {attack}")
    print(f"Health: {hp}")







while hp > 0:
    TextSpacer(2)
    MobDisplay()
    TextSpacer(2)
    PlayerDisplay()
    action = input("Attack(a): ")
    if mob_hp <= 0:
        MobGen()
    if action.lower() == "a":
        hp -= mob_attack
        mob_hp -= attack
        TextSpacer(2)
        MobDisplay()
        TextSpacer(2)
        PlayerDisplay()

    else:
        quit()






