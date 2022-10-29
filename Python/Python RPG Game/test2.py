
from hashlib import new


class EnemyConstructor():
    def __init__(self, name=None, hp=None, attack=None, magic_attack=None, defence=None, magic_defence=None, speed=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.magic_attack = magic_attack
        self.defence = defence
        self.magic_defence = magic_defence
        self.speed = speed


#enemy = EnemyConstructor("Slime", 10, 2, 2, 0, 0, 1)


def RoomStatsReader(room_index):
    f_data_lists = []
    with open(f"Rooms/{room_index}.txt") as f:
        data_lists = f.read().split(",")
        for i in data_lists:
            f_data_lists.append(i.strip()) 
        

        return f_data_lists
    
