#!/usr/bin/python

''' Allows user to input annual salary -
program should output monthly gross salary '''

def multiply(num1, num2):
    answer = num1 * num2
    return answer

def divide(num1, num2):
    return num1 / num2

def monthly_salary(gross):
    return divide(gross, 12)

def after_tax(tax_rate, gross):
    return gross - (multiply(gross, divide(tax_rate, 100)))

total_salary = int(input("How much a year do you earn  £"))
tax_rate = float(input("What is the tax rate as a percent "))

print("Your salary per month is ", monthly_salary(total_salary))
print("Your salary per year after tax is ",after_tax(tax_rate, total_salary))
print("Your salary per month after tax ", monthly_salary(after_tax(tax_rate, total_salary)))
