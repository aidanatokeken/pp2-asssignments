#Write a Python program to convert degree to radian. Input degree: 15Output radian: 0.261904
import math
d = float(input("Input degree: "))
r = d * (math.pi / 180)
print("Output radian:", round(r, 6))

#Write a Python program to calculate the area of a trapezoid.Height: 5 Base, first value: 5 Base, second value: 6
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
a = (base1 + base2) / 2 * height
print("Expected Output:", a)

#Write a Python program to calculate the area of regular polygon.Input number of sides: 4Input the length of a side: 25 The area of the polygon is: 625
import math
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
a = (n * s ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", round(a))

#Write a Python program to calculate the area of a parallelogram.Length of base: 5Height of parallelogram: 6Expected Output: 30.0
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print("Expected Output:", area)