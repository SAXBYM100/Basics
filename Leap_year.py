#!/usr/bin/python

'''Calculating input from user and determining if it is a leap year'''

# This function takes the user input as an int
def year_input():
    year = int(input('input year: '))
    return year

get_year = year_input()

while True:
        if (get_year % 400 == 0) and (get_year % 100 == 0):
             print(get_year, 'is a leap year')
             break
        else:
             print('Thats not a leap year! Try again')
        get_year = year_input()
