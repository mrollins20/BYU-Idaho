# Marc Rollins
# Week 1 prove assignment

import math

print('> python tire_volume.py')

tire_width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
wheel_diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

tire_volume = (math.pi*(tire_width*tire_width)*aspect_ratio*(tire_width*aspect_ratio+2540*wheel_diameter))/10000000000

print(f'The approximate volume is {tire_volume:.2f} liters.')