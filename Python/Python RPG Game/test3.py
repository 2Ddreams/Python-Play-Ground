import random
def RoomStatsReader(room_index):
    f_data_lists = []
    with open(f"Rooms/{room_index}.txt") as f:
        data_lists = f.read().split(",")
        for i in data_lists:
            f_data_lists.append(i.strip()) 
        

        return f_data_lists


num_of_mobs = RoomStatsReader(0)[0]
mob_names = []
for i in range(1,len(RoomStatsReader(0)), 7):
    mob_names.append(RoomStatsReader(0)[i])
print(mob_names)

