
from functools import total_ordering


months_list = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date_dict = {}

days_total = 0

def TextSpacer(lines):
    if lines == "blank":
        print(" ")
    else: 
        for i in range(lines):
            print("----------------------------------------------------------------")

# List Combinator
def ListCombinator(list_name, list_num):
    for i in range(len(list_name)):
        date_dict[list_name[i]] = list_num[i]

ListCombinator(months_list, days)
    
print(date_dict)
TextSpacer(2)
start_month = input("Starting Month: ") 
start_date = int(input("Starting Date:  "))
TextSpacer(1)
end_month = input("Ending Month: ")
end_date = int(input("Ending Date:  "))
TextSpacer(2)



if end_month == start_month:
    end_date -= start_date
    print(f"You have {end_date}(s) left")
elif end_month != start_month:
    start_index = months_list.index(start_month.lower()) + 1
    end_index = months_list.index(end_month.lower())
    for i in range(start_index, end_index):
        days_total += days[i]
    days_total += date_dict.get(start_month.lower()) - start_date
    days_total += end_date
    
    print(start_index, end_index)
    print(days_total)
