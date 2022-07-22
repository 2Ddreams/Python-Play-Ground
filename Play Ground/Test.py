
letter_check_display = {0: 'cpcl', 1: 'cpcl', 2: 'cpcl', 3: 'cpcl', 4: 'cpcl'}

check_list = []

for i in range(len(letter_check_display)):
    letter_check_display[i] = True
    check_list.append(letter_check_display.get(i))

print(letter_check_display)
print(check_list)


if all(check_list):
    print("YES")
else:
    print("NO")