import math 

def factorise (a, b, c):
  x = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 *a
  x2 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 *a
  return x, x2

def symmetry (a, b):
  x =  (-1 * b) / (2 * a)
  return x

def vertex_point_y (a, b, c, x):
  y =  a * (x * x) + b * x + c
  return y
try:
  a = float(input("a value: ")) 
  b = float(input("b value: ")) 
  c = float(input("c value: ")) 
  print("")
  print(f"y = {a}x^2 + {b}x + {c}")
  x = symmetry(a, b)
  print("")
  print(f"X-intercepts: {factorise(a, b, c)}")
  print(f"Axis of symmetry: x = {symmetry(a, b)}")
  print(f"Vertex point: ({x},{vertex_point_y(a, b, c, x)})")
  print(f"y-intercept: {c}")
except:

  print("Detected parabola with no x-intercept")
  print("")
  print(f"y = {a}x^2 + {b}x + {c}")

  x =  (-1 * b) / (2 * a)

  y =  a * (x * x) + b * x + c

  print(f"x = {x}, y = {y}")

  print(f"y-intercept: {c}")

