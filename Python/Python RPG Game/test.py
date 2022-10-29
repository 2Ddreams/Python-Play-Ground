def GetKey(key):
    data_set = ["abcdefghijklmnopqrstuvwxyz"]
    lowered_key = key.lower().strip()
    print(lowered_key)
    if lowered_key in data_set:
        return lowered_key
    else: 
        return "Invalid Move!"


if "a" in "iloveu":
    print("yes")
else:
    print('no')
user_ipnut = input("k: ")
print(GetKey(user_ipnut))

