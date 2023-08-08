from math import pi

def area_of_circle(r):
    if r < 0:
        raise ValueError("The radius cannot be negative")
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number")
    
    return pi * (r**2)

print(area_of_circle(1))