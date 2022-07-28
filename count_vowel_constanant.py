#!/usr/bin/python

''' Allows user to input string
determines vowels, constanants '''

# functio to allow user to input a string

def ask_for_str():
    string_from_user = str(input('Please provide a word/sentence: '))
    return string_from_user

# function to check if user input character is in vowel list
def character_check(start_num, items_to_compare, thing_to_check):
    for ch in items_to_compare:
        start_num += thing_to_check.lower().count(ch)
    return start_num

vowel_item = 'aeiou'
consontant_item = 'qwrtypsdfghjklzxcvbnm'

string_to_check = ask_for_str()

how_many_vowels = character_check(0,vowel_item,string_to_check)
how_many_constonants = character_check(0,consontant_item, string_to_check)

print(f"Number of vowels {how_many_vowels}, the number of constonants {how_many_constonants}")

# list of vowels

#
#vowel_num = vowel_check(0)

