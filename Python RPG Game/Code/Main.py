import random
import os

player_normal_attack_energy_cost = 1
game_state = False

def RoomStatsReader(room_index):
    f_data_lists = []
    with open(f"Rooms/{room_index}.txt") as f:
        data_lists = f.read().split(",")
        for i in data_lists:
            f_data_lists.append(i.strip()) 
        
        return f_data_lists

print(RoomStatsReader(0))

class EnemyConstructor():#1         #2          #3              #4              #5            #6                   #7         #8
    def __init__(self, name=None, hp=None, attack=None, magic_attack=None, defence=None, magic_defence=None, speed=None, heal_amount=1):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.magic_attack = magic_attack
        self.defence = defence
        self.magic_defence = magic_defence
        self.speed = speed
        self.heal_amount = random.randrange(1, heal_amount+1)


enemy = EnemyConstructor("No Enemy", 0, 0, 0, 0, 0, 0)

class Player():         #1                  #2          #3                 #4              #5            #6                      #7             #8             $9           #10   
    def __init__(self, name=None, current_health=None, max_health=None, attack=None, magic_attack=None, defence=None, magic_defence=None, speed=None, cur_energy=None, max_energy=None,):
        self.name = name
        self.cur_hp = current_health
        self.max_hp = max_health
        self.attack = attack
        self.magic_attack = magic_attack
        self.defence = defence
        self.magic_defence = magic_defence
        self.speed = speed
        self.cur_energy = cur_energy
        self.max_energy = max_energy


player = Player("Explorer", 100, 100, 10, 5, 1, 0, 1, 10, 10)

class Weapon():            #1               #2       #3          #4             #5              #6             #7
    def __init__(self, name="Weapon", damage=0, magic_damage=0, defence=0, magic_defence=0, energy_cost=0, speed=0):
        self.name = name
        self.damage = damage
        self.magic_damage = magic_damage
        self.defence = defence
        self.magic_defence = magic_defence
        self.energy = energy_cost
        self.speed = speed

weapon = Weapon("Stone Sword", 2, 0, 1, 0, 0, 1)


def ClearScreen():
    os.system("cls")

def CheckKey(key):
    lowered_key = key.lower()
    if lowered_key == "a":
        return "Attacked!"
    elif lowered_key == "d":
        return "Defended!"
    else: 
        return "Invalid Move!"

def GetKey(key):
    lowered_key = key.lower()
    if lowered_key == "a":
        return "a"
    elif lowered_key == "d":
        return "d"
    elif lowered_key == "h":
        return "h"
    elif lowered_key == "esc":
        
        exit()
    else: 
        return "Invalid Move!"



def DisplayGUI(display_text="", display_text2="",display_text3="", display_text4="", enemy=enemy, player=player, weapon=weapon, enemy_left=0, room_index=0):
    ClearScreen()
    if player.cur_hp > player.max_hp:
        player.cur_hp = player.max_hp
    if player.cur_energy > player.max_energy:
        player.cur_energy = player.max_energy
    print(f"----------------------------------------------------------------")
    print(f"| Name: [{player.name}]  [Health: {player.cur_hp}/{player.max_hp}]  [Energy: {player.cur_energy}/{player.max_energy}]")
    print(f"| Attack: [{player.attack}+({weapon.damage})|{player.magic_attack}+({weapon.magic_damage})]  Defence: [{player.defence}+({weapon.defence})|{player.magic_defence}+({weapon.magic_defence})]  Speed: [{player.speed}+({weapon.speed})]")
    print(f"|--------------------------------------------------------------|")
    print(f"| Enemy Left: [{enemy_left}]  Room: [{room_index}]")
    print(f"| Weapon: [{weapon.name}]  Energy Cost: [{weapon.energy}]")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"| Enemy: [{enemy.name}]                                                       ")
    print(f"| Health: [{enemy.hp}]  Attack: [{enemy.attack}]  Defence: [{enemy.defence}|{enemy.magic_defence}]")
    print(f"| Speed: [{enemy.speed}]                                                            ")
    print(f"|--------------------------------------------------------------|")#
    print(f"| {display_text}")
    print(f"| {display_text2}")
    print(f"| {display_text3}")
    print(f"| {display_text4}")
    user_input = input(f"| Input: ")
    print(f"----------------------------------------------------------------")
    return user_input

def CalabrationFunction():
    print("<---------------------------------------------------------------->")
    print("Make sure this line is striaght across your screen. ")
    input("Press Enter To Continue...\n")
    print(f"^                                                              ^")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"|                                                              |")
    print(f"_                                                              _")
    print("\nMake sure all lines are visible on your screen.")
    input("Press Enter To Continue...\n")


def AwaitInput():
    input("Press Any Key To Continue...\n")
    input("")

def Attack(energy_cost, target, player, weapon, upgrade=0, energy_upgrade=0):
    if player.cur_energy + energy_upgrade >= energy_cost + weapon.energy:
        player.cur_energy -= energy_cost + weapon.energy
        target.hp -= (player.attack + weapon.damage + upgrade) - target.defence
    else:
        return "You Don't Have Enough Energy To Attack"

def AttackPlayer(enemy, player):
    player.cur_hp -= enemy.attack
    
def DefendSequence(player, enemy, weapon, upgrade=0):
    player.cur_energy += 4 + upgrade
    player.cur_hp -= enemy.attack-player.defence + (weapon.defence)

def Heal(player, weapon, heal_amount, energy_cost, upgrade=0):
    player.cur_hp += player.attack * heal_amount + weapon.damage + upgrade
    player.cur_energy -= energy_cost + weapon.energy


def EnemySpawner(room_index=0):
    mob_names = [] 
    for i in range(1,len(RoomStatsReader(room_index)), 8):
        mob_names.append(RoomStatsReader(room_index)[i])
        random_num = random.randrange(1, len(mob_names)+1)
        if random_num == 1:
            enemy = EnemyConstructor(RoomStatsReader(room_index)[1], float(RoomStatsReader(room_index)[2]), float(RoomStatsReader(room_index)[3]), float(RoomStatsReader(room_index)[4]), float(RoomStatsReader(room_index)[5]), float(RoomStatsReader(room_index)[6]), float(RoomStatsReader(room_index)[7]), float(RoomStatsReader(room_index)[8]))
        if random_num == 2:
            enemy = EnemyConstructor(RoomStatsReader(room_index)[9], float(RoomStatsReader(room_index)[10]), float(RoomStatsReader(room_index)[11]), float(RoomStatsReader(room_index)[12]), float(RoomStatsReader(room_index)[13]), float(RoomStatsReader(room_index)[14]), float(RoomStatsReader(room_index)[15]), float(RoomStatsReader(room_index)[16]))
        if random_num == 3:
            enemy = EnemyConstructor(RoomStatsReader(room_index)[17], float(RoomStatsReader(room_index)[18]), float(RoomStatsReader(room_index)[19]), float(RoomStatsReader(room_index)[20]), float(RoomStatsReader(room_index)[21]), float(RoomStatsReader(room_index)[22]), float(RoomStatsReader(room_index)[23]), float(RoomStatsReader(room_index)[24]))
    return enemy

    


def GameManager(room_index=0, player=player):
    num_of_mobs = RoomStatsReader(room_index)[0]
    for i in range(int(num_of_mobs)):
        enemy = EnemySpawner(room_index)
        player.cur_hp += enemy.heal_amount
        print(enemy.hp)
        while player.cur_hp > 0 and int(enemy.hp) > 0:
            user_input = DisplayGUI(f"You Encountered a [{enemy.name}]", f"ATTACK!", "Attack(a) | Defend(d) | Heal(h)", " ", enemy, player, weapon, int(num_of_mobs)-i, room_index)
            action =  GetKey(user_input)
            display_action = CheckKey(user_input)
            if enemy.hp > 0:
                if action == "a":
                    if player.cur_energy >= player_normal_attack_energy_cost + weapon.energy:
                        if player.speed > enemy.speed:
                            Attack(player_normal_attack_energy_cost, enemy, player, weapon)
                            Attack((player_normal_attack_energy_cost, enemy, player, weapon)*0.6)
                        else:
                            Attack(player_normal_attack_energy_cost, enemy, player, weapon)
                        if enemy.hp > 0:
                            if enemy.speed > 2*player.speed:
                                AttackPlayer(enemy, player)
                                AttackPlayer((enemy, player)*0.5)
                            else:
                                AttackPlayer(enemy, player)

                    else:
                        DisplayGUI("You Do Not Have Enough Energy", "", "", "You Can Defend To Gain Energy", enemy, player, i, room_index)
                elif action == "d":
                    DefendSequence(player, enemy, weapon)
                elif action == "h":
                    Heal(player, weapon, 0.6, 2)
                    
                else:
                    print(action)
            else:
                player.cur_hp += enemy.heal_amount


        
player = Player("Explorer", 100, 100, 10, 5, 1, 0, 1, 10, 20)


ClearScreen()
CalabrationFunction()
name = DisplayGUI("What is your name?")
while name == "":
    name = DisplayGUI("What is your name?")
name = name.upper()
player.name = name
DisplayGUI(f"Hello {name}!", "Press enter to continue...")
DisplayGUI(f"Welcome to this adventure", f"This window will be where everything is displayed")


while player.cur_hp > 0 and game_state == False:
    player = Player("HERE", 111, 111, 11, 1, 1, 1, 1, 11, 11)
    DisplayGUI("Rules:","Your Stats Are Shown On The Top Of the Screen", "Every Time A Enemy Spawns You Will Heal A", "Random Amount from 1 to the enemies max HP ", enemy, player)
    DisplayGUI("Things To Know:","You Can Not Retreat.", "Your Only Way Forward Is ATTACKK!", " ", enemy, player)
    enemy = EnemyConstructor("HERE", 1, 1, 1, 1, 1, 1)
    DisplayGUI("Things To Know:", "Enemy Stats Will Show Up Here", "Each Time You Do An Action", "IT Will Use A Certain Amount Of Energy", enemy, player)
    DisplayGUI("When In Battle You will Be Prompted With Something Like This", "ATTACK!", "Attack(a) | Defend(d) | Heal(h)", "", enemy, player)
    DisplayGUI("Next We Will Do A Simple Practice", "Let's Rest Your Stats!", "", "", enemy, player)
    player = Player(name, 100, 100, 10, 5, 1, 0, 1, 10, 20)
    enemy = EnemyConstructor("No Enemy", 0, 0, 0, 0, 0, 0)
    



    GameManager(0, player)
    GameManager(1, player)
    GameManager(2, player)
    #GameManager(3, player)
    #GameManager(4, player)
    #GameManager(5, player)





print("dead")
