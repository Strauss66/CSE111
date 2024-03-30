import math 
w = int(input("Enter the width of the tire in mm: "))
a = int(input("Enter the aspect ratio of the tire: "))
d = int(input("Enter the diameter of the wheel in inches: "))
volume = (math.pi * w**2 * a * (w*a + 2540*d)) / 10000000000
print (f"The approximate volume is {volume:.2f} liters")