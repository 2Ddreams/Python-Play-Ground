import math
import matplotlib.pyplot as plt



def ParabolaPlotting():
    midpoint = 0
    x_int = 0, 0
    y_int = 0
    axis_symmetry = 0

def QuadraticSolver(a, b, c):
    x1 = (-(b) + math.sqrt((b*b) - 4 * a * c))/2*a
    x2 = (-(b) - math.sqrt((b*b) - 4 * a * c))/2*a
    return x1, x2


class Parabola():
    def __init__(self, a, b, c):
        self.midpoint = -(b)/2*a
        self.x_int1 = QuadraticSolver(a, b, c)[0]
        self.x_int2 = QuadraticSolver(a, b, c)[1]
        self.y_int = (a * 0) + (b * 0) + c
        self.axis_symmetry = (-(b))/2*a





x = [0, 12, 3, 4, 5, 6]
y = [0, 45, 5, 5, 5, 2]

plt.title("WHY")

plt.xlabel("X - axis")
plt.ylabel("Y - axis")






#plt.savefig("test.png", dpi=300)
plt.show()


