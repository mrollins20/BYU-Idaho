# Marc Rollins
# Week 02 Prove Assignment: Calling Functions

# All prices use in this program are based on discounttire.com

# Calls for the date and time from the system
from datetime import datetime
# Calls for specific math formulas
import math

user_choice = 'yes'
tire_cost = 0

while user_choice.lower != 'no':
# Sets the current date and time from the system to the variable 'current_time'
    current_time = datetime.now()

    print('> python tire_volume.py')

    # User is prompted for inputs on tires
    tire_width = int(input('Enter the width of the tire in mm (ex 205): '))
    aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
    wheel_diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

    # tire volume is calculated
    tire_volume = (math.pi*(tire_width*tire_width)*aspect_ratio*(tire_width*aspect_ratio+2540*wheel_diameter))/10000000000
    log = str(f'{current_time:%y-%m-%d}, {tire_width}, {aspect_ratio}, {wheel_diameter}, {tire_volume:.2f}')

    print(f'The approximate volume is {tire_volume:.2f} liters.')
    print()

    inquire_cost = 'Would you like to know the price of these tires? (yes or no): '

    if inquire_cost.lower == 'yes':
        tire_type = int(input('What kind of tire are you interested in? (all-season [1], winter/snow [2], all-terrain [3], performance [4]: '))
        
        if wheel_diameter >= 12:
            # all-season cost at 12-15in
            if tire_type == 1:
                tire_cost = str('$80-$150')
                print(f'The average cost per small, all-season tire is {tire_cost}.')
            # winter/snow cost at 12-15in
            elif tire_type == 2:
                tire_cost = str('$100-$150')
                print(f'The average cost per small, winter/snow tire is {tire_cost}.')
            # all-terrain cost at 12-15in
            elif tire_type == 3:
                tire_cost = str('sorry, this type of tire is unavailable in this size.')
                print(tire_cost)
            # performance cost at 12-15in
            elif tire_type == 4:
                tire_cost = str('sorry, this type of tire is unavailable in this size.')
                print(tire_cost)
        elif wheel_diameter >= 16:
            # all-season cost at 16-20in
            if tire_type == 1:
                tire_cost = str('$100-$250')
                print(f'The average cost per medium, all-season tire is {tire_cost}.')
            # winter/snow cost at 16-20in
            elif tire_type == 2:
                tire_cost = str('$200-$400')
                print(f'The average cost per medium, winter/snow tire is {tire_cost}.')
            # all-terrain cost at 16-20in
            elif tire_type == 3:
                tire_cost = str('$150-$250')
                print(f'The average cost per medium, all-terrain tire is {tire_cost}.')
            # performance cost at 16-20in
            elif tire_type == 4:
                tire_cost = str('$100-$750 (This type of tire can vary greatly in cost.)')
                print(f'The average cost per medium, performance tire is {tire_cost}.')
        elif wheel_diameter >= 20:
            # all-season cost at 18-26in
            if tire_type == 1:
                tire_cost = str('$140-$170')
                print(f'The average cost per large, all-season tire is {tire_cost}.')
            # winter/snow cost at 18-26in
            elif tire_type == 2:
                tire_cost = str('sorry, this type of tire is unavailable in this size.')
                print(tire_cost)
            # all-terrain cost at 18-26in
            elif tire_type == 3:
                tire_cost = str('$200-$500')
                print(f'The average cost per large, all-terrain tire is {tire_cost}.')
            # performance cost at 18-26in
            elif tire_type == 4:
                tire_cost = str('$200-$1000')
                print(f'The average cost per large, performance tire is {tire_cost}.')

    # Asks the user if they would like to buy the current tires
    save_phone_number = str(input('Would you like to buy tires in these dimensions (yes or no)? '))

    # Saves the users phone number for reference
    if save_phone_number.lower() == 'yes':
        phone_number = str(input('Please enter your phone number here: '))
        log = str(f'{current_time:%y-%m-%d}, {tire_width}, {aspect_ratio}, {wheel_diameter}, {tire_volume:.2f}, [{tire_type}, {tire_cost}, {phone_number}]')
    
    # opens and writes data to tire_volume.txt
    volume_log = open('tire_volume.txt', 'at')
    volume_log.write(f'{log}\n')
    print('Data stored successfully!')

    user_choice = str(input('Would you like to continue (yes or no)? '))

    while user_choice != ('yes' or 'no'):
        print("That response was't a possible response, please respond with yes or no.")
        user_choice = str(input('Would you like to continue?'))

print()
print('Thank you for using tire_volume.py')