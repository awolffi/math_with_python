import numpy as np

a = 2.493
b = 0.911
c = 137.7
d = 62.3

print(f"2.493 rad is {np.degrees(a)} degrees")
print(f"0.911 rad is {np.degrees(b)} degrees")
print(f"137.7 deg is {np.radians(c)} rad")
print(f"62.3 deg is {np.radians(d)} rad")

A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
print("////////////////////////////")
for i in A:
  print(f"{i} deg is {np.radians(i)} rad")

print("///////////////////////")
x = 1.6
y = 2.3
hypotenuse = np.hypot(x, y)

# Print the result
print(f"hypotenuusan pituus kun kateetit ovat 1.6 ja 2.3 on: {hypotenuse}")