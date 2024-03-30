import math

def main():
    names = ["#Picnic","# Tall","#2","#2.5","#Cylinder","#5","#6Z","8Z short", "#10","#211","#300","#303"]
    radius = [6.83,7.78,8.73,10.32,10.79,13.02,5.40,6.83,15.72,6.83,7.62,8.10]
    height = [10.16,11.91,11.59,11.91,17.78,14.29,8.89,7.62,17.78,12.38,11.27,11.11]
    cost_per_can = [0.28,0.43,0.45,0.61,0.86,0.83,0.22,0.26,1.53,0.34,0.38,0.42]

    for i in range(len(names)):
        volume = calc_volume(radius[i], height[i])
        surf_area = calc_surface(radius[i], height[i])
        storage_ef = calc_storage(volume, surf_area)
        print(f"Name: {names[i]}. \n Volume: {volume:.2f}.\n Surface Area: {surf_area:.2f}. \n Storage efficiency: {storage_ef:.2f}")

def calc_volume(r, h):
    volume = math.pi * r**2 * h
    return volume

def calc_surface(r, h):
    """
    Calculate the surface area of the can.

    Parameters: 
    r(float): Radius of the can.
    height(float): Height of the can.
    """
    surface_area = 2 * math.pi * r * (r + h)
    return surface_area

def calc_storage(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

main()

"""
We could've used another for to loop thru the list
for i, name enumerate(names):
age    = ages[i]
    gender = genders[i] 
    print(f"Name: {name:<15} Age: {age:<5} Gender: {gender}")
"""