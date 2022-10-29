import math
import matplotlib.pyplot as plt


x = []
y = []

def FibonacciSequencer(num_of_lines):
    num1 = 0
    num2 = 1
    for i in range(num_of_lines):
        y.append(num2)
        x.append(i)
        num_sum = num1 + num2
        num1 = num2 
        num2 = num_sum
num_of_lines = int(input("Number Of Lines Of Fibonacci Sequence: "))

FibonacciSequencer(num_of_lines)

plt.plot(x, y)
plt.show()