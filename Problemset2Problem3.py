# -*- coding: utf-8 -*-
"""
Write a program that uses bisection search to find the smallest monthly payment 
to the cent such that we can pay off the debt within a year.
"""

balance = 320000
annualInterestRate = 0.2
initBalance = balance
monthlyInterestRate = annualInterestRate/12.0
low = balance/12.0
high = (balance * ((1.0 + monthlyInterestRate)**12))/12.0
epsilon = 0.01
minPay = (high + low)/2.0
month = 0

def calculate(month, balance, minPay, monthlyInterestRate):
    while month <12:
        unpayBalance = balance - minPay
        balance = unpayBalance + (monthlyInterestRate * unpayBalance)
        month += 1 
    return balance

while abs(balance) >= epsilon:
    balance = initBalance
    month = 0
    balance = calculate(month, balance, minPay, monthlyInterestRate)
    if balance > 0:
        low = minPay
    else:
        high = minPay
    minPay = (high + low)/2.0

minPay = round(minPay,2)
print('Lowest Payment: ' + str(minPay))