#!/usr/bin/python
import re

'''This is a password checker, takes a input and checks against three rules,
the password needs at least 8 char, one capital letter and at least one lower case letter'''

#function to take input
def pass_input():
    password_input = (input('input password: '))
    return password_input

#takes return of function and sets in the password_user
password_user = pass_input()

#function to test_password user against length, capitals and lowercase
def char_length(password_user):
    if len(password_user) < 8:
        print('This password is incorrect')
    elif re.search(password_user, '[A-Z]') is None:
        print('This password is incorrect')
    elif re.search(password_user, '[a-z]') is None:
        print('This password is incorrect')
    else:
        print('password accepted')

char_length(password_user)

