from datetime import datetime

current_date_and_time  = datetime.now()
day_of_week = current_date_and_time.weekday()
day_of_week = 2

print(day_of_week)

get_subtotal = float(input('Please enter the subtotal:  '))


if day_of_week == 1 or day_of_week == 2:
    if get_subtotal >= 50:
        get_subtotal = get_subtotal*0.9

sales_tax_amount = get_subtotal * 0.06 

total = get_subtotal + sales_tax_amount

print(f'Sales tax amount:  {sales_tax_amount:.2f}')
print(f'Total: {total:.2f}')

