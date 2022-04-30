# Marc Rollins
# Week 02, Calling Functions

import math

print('> python boxes.py')

# Asks user for information
item_count = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

# Calculates the number of boxes needed
number_of_boxes = math.ceil(item_count / items_per_box)

# Displays the result to the user
print()
print(f'For {item_count} items, packing {items_per_box} items in each box, you will need {number_of_boxes} boxes.')