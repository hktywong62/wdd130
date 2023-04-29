'''
author:  TY Wong
file:  02 Prove : Callings Functions

purpose:  write a program that calls functions and methods to get the current date
          and append values to a text file with an exceeding requirement

'''
          

# to write a program to get the inputs from the user for calculating the approximate volume

import math

width = float(input('Enter the width of the tire in mm:   '))
aspect_ratio = float(input('Enter the aspect ratio of the tire:  '))
diameter  = float(input('Enter the diameter of the wheel in inches:   '))


def calculate_volume(width, aspect_ratio, diameter):
    return math.pi*(width**2)*aspect_ratio*(width*aspect_ratio + 2540*diameter)/10000000000

print()

print(f'The approximate volume is {calculate_volume(width, aspect_ratio, diameter):.2f} liters.')

#Follow-up actions (an exceeding requirement)

followup_action = input('Do you want to buy tires with the dimentsions that you enter, yes or no?   ')

phone_no = '00000000'

if followup_action == 'no':
    print('You are welcome.')
if followup_action =='yes':
    phone_no = input('Please leave your phone number for record:   ')


#import the datetime class from the datetime module so that it can be used in this program.

from datetime import  datetime

#Call the now() method to get the current
#date and time as a datetime object from
#the computer's operating system.

curremt_date_and_time = datetime.now()

#Use an f-string to print only the date
#part of the current date and time

print(f'{curremt_date_and_time:%Y-%m-%d}')

#open the volumes.txt in append mode and write the values on the file.

with open('volumes.txt', 'at') as volumes_file:
    print(f'{curremt_date_and_time:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {calculate_volume(width, aspect_ratio, diameter):.2f}, {phone_no}', file=volumes_file)
          



