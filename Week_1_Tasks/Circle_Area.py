import os
import numpy as np

def Area(radius):
    return np.pi * (radius**2)

radius = input("Circle Radius : ")   
print(f"Area of the Circle = {Area(float(radius))}")

