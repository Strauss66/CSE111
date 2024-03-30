import math 
from datetime import datetime, timedelta
w = int(input("Enter the width of the tire in mm: "))
a = int(input("Enter the aspect ratio of the tire: "))
d = int(input("Enter the diameter of the wheel in inches: "))
volume = (math.pi * w**2 * a * (w*a + 2540*d)) / 10000000000
print (f"The approximate volume is {volume:.2f} liters")
current_date = datetime.now().strftime("%Y/%m/%d")
#The prizes are from Walmart.com
if w == 185: 
    prize = 53.00
    print(f"The price is: ${prize}")
elif w == 205:
    prize = 60.44
    print(f"The price is: ${prize}")
elif w == 225:
    prize = 128.93
    print(f"The price is: ${prize}")
else: 
    print("We currently don't have that size! Sorry!")
with open("/Users/Ing.Armando/Documents/College 2nd Semester/Programming with Functions CSE111/Week 2/volumes.txt", mode="a") as volumes_file:
    print(f"{current_date}, {w}, {a}, {d}, {volume:.2f} prize: ${prize}: ",file=volumes_file) 