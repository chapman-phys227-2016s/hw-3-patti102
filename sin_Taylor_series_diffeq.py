#! /usr/bin/env python

"""
File: loan.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module calculates Taylor Series expansion of sin and produces a table
for various values of x and approximation term numbers.

"""

from math import sin, fabs

def sin_Taylor(x, n):
    """Returns the Taylor Series of sin at x calculated up to the nth order term."""
    s = 0
    a = x
    for n in range(1, n+1):
        s = s + a
        a = a * (-(x**2) / float(((2*n + 1) * 2 * n)))
    return s, fabs(a)

def table():
    """Outputs a table for list of x and n values as well as their errors as calculated
    by the approximation minus the actual value of sin at that location."""
    x_list = [0.2, 1.57, 3.14]
    n_list = [2, 4, 10]
    print
    print '%15s %15s %20s %20s' % ('X-Value', 'N-Value', 'Approx', 'Error')
    print
    for x in x_list:
        for n in n_list:
            data = sin_Taylor(x, n)
            print '%15f %15d %20f %20f' % (x, n, data[0], data[0] - sin(x))
            print

def test_sin_at_zero():
    """Ensures that the sin of zero in the approximation is zero."""
    apt = fabs(sin_Taylor(0, 1000)[0]) < 1e-3
    msg = 'Sin at zero is not zero.'
    assert apt, msg
    
def test_two_terms():
    """Tests that the approximation of sin at x = 0.01 for two terms is correct as per
    the definition of the Taylor Series and its calculation at the point x = 0.01"""
    apt = fabs(sin_Taylor(0.01, 2)[0] - 0.00999983) < 1e-3
    msg = 'Sin at 0.01 for n of 2 is not accurate.'
    assert apt, msg