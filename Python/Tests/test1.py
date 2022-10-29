from tkinter import Y


def shift_to_right(x, y):
    ans = x/(2**y)
    return int(ans)

print(shift_to_right(80, 3))
