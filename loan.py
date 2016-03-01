#! /usr/bin/env python

"""
File: loan.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module calculates the vectors containing both the remaining values of a loan and the monthly
payments given as a function of total loan amount, yearly interest rate, and total number of payment
months with the understanding that monthly interest be added to the total portion of principle paid each
month such that principle decrease is linear.

"""

import numpy as np

def loan_calculator(L, p, N):
    """Calculates the total loan amount and monthly payment for a given loan value, yearly interest
    rate, and borrowing period."""
    payments = np.zeros(N + 1)
    loan_amount = np.zeros(N + 1)
    interest_month = p / float(12 * 100)
    payment_month = L / float(N)
    payments[0] = 0
    loan_amount[0] = L
    for n in range(1, N + 1):
        payments[n] = interest_month * loan_amount[n - 1] + payment_month
        loan_amount[n] = loan_amount[n - 1] * (1 + interest_month) - payments[n]
    return loan_amount, payments

def test_loan_amortized():
    """Ensures that the loan is properly paid off at the end of the lending period."""
    apt = abs(loan_calculator(1000, 10, 10)[0][-1]) < 1e-3
    msg = 'Loan not amortized.'
    assert apt, msg