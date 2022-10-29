list_of_num = []

nums = input("Number: ")

list_of_num.append(int(nums))
while nums != " ":
    nums = int(input("Number: "))
    list_of_num.append(int(nums))


print(list_of_num)