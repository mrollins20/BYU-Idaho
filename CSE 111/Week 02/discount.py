# Marc Rollins
# Week 02 Team Assignment

# Import date and time
from datetime import datetime

# Call the date and time
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

print('> python discount.py')
user_choice = 'yes'
while user_choice != 'no':
    subtotal = float(input('Please enter the subtotal: '))

    sales_tax = subtotal * 0.06
    total = sales_tax + subtotal

    if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
        discount_amount = 0.1 * subtotal
        discount = 0.9 * subtotal
        discount_tax = discount * 0.06
        discount_total = discount + discount_tax
        print(f'Discount amount: {discount_amount:.2f}')
        print(f'Sales tax amount: {discount_tax:.2f}')
        print(f'Total: {discount_total:.2f}')

    else:
        print(f'Sales tax amount: {sales_tax:.2f}')
        print(f'Total: {total:.2f}')
    
    user_choice = str(input('Would you like to continue (yes or no)? '))

# Print the day of the week for the user
# print(current_date_and_time)
# print(day_of_week)