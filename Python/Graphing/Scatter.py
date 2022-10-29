import matplotlib.pyplot as plt



x = [10, 4, 6, 8, 9, 5, 7, 1, 2, 3]
y = [20, 6, 8, 13, 20, 12, 13, 4, 2, 7]

plt.scatter(x, y)

plt.savefig("test.png")
plt.show()
