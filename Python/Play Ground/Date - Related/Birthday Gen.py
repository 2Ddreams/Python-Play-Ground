import random

months_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


date_dict = {}


def RandomNumGen(start, stop):
    num = random.randrange(start,stop+1)
    return num

for i in range(len(months_list)):
    date_dict[months_list[i]] = RandomNumGen(1, days[i])


year = RandomNumGen(1760, 2022)
month = random.choice(months_list)
date = date_dict.get(month)

print(f"On the year {year} and {date} of {month}")