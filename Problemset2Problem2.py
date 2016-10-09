# -*- coding: utf-8 -*-
"""
Write a program that calculates the minimum fixed monthly payment needed in 
order pay off a credit card balance within 12 months.
"""

balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
month = 0
minPay = 10
def calculate(month, balance, minPay, monthlyInterestRate):
    while month <12:
        unpayBalance = balance - minPay
        balance = unpayBalance + (monthlyInterestRate * unpayBalance)
        month += 1 
    return balance
    
while calculate(month, balance, minPay, monthlyInterestRate) > 0:
    minPay +=10
    month = 0
    calculate(month, balance, minPay, monthlyInterestRate)

print('Lowest Payment: ' + str(minPay))
