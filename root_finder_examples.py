#!  /usr/bin/env python

"""
File: root_finder_examples.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module calculates the approximate value for function roots and then verifies
these values by presenting a table with the root value and the value of the function
at that point all while comparing three different algorithmic techniques.

"""

import sys
from math import *
import sympy as sp

def run(func, prime, A, B, xzero, xone):

    f = eval(sys.argv[1])
    f_prime = eval(sys.argv[2])
    a = float(sys.argv[3])
    b = float(sys.argv[4])
    x_0 = float(sys.argv[5])
    x_1 = float(sys.argv[6])

    f_eval = f(x_0)
    n = 0
    data = [(x_0, f_eval)]
    x_copy = x_0
    while abs(f_eval) > 1e-6 and n<=1000:
        diff_eval = float(f_prime(x_copy))
        if abs(diff_eval) < 1e-9:
            raise ValueError("Derivative too small for safe division.")
        x_copy = x_copy - f_eval / float(diff_eval)
        n = n + 1
        f_eval = f(x_copy)
        data.append((x_copy, f_eval))

    f_eval_bis_a = f(a)
    data_bis = ([a, f_eval_bis_a])
    if f_eval_bis_a * f(b) > 0:
        m = (a+b)/2.0
        data_bis.append((m, f(m)))
    else:
        n = 0
        while b - a > 1e-5:
            n = n + 1
            m = (a + b) / 2.0
            fm = f(m)
            if f_eval_bis_a * fm <=0:
                b = m
            else:
                a = m
                fa = fm
            data_bis.append((m, fm))

    f_eval_sec = f(x_0)
    n = 0
    data_sec = [(x_0, f_eval_sec)]
    x_0_copy = x_0
    x_1_copy = x_1
    for n in range(1, 1001):
        if abs(float(x_1_copy - x_0_copy)) < 1e-14:
            print
            print '%20s %20s %20s' % ('Root Finder Type', 'X-approximation', 'Function Value')
            print
            print '%15s %20f %20f' % ('Newton', data[-1][0], data[-1][1])
            print
            print '%15s %20f %20f' % ('Bisector', data_bis[-1][0], data_bis[-1][1])
            print
            print '%15s %20f %20f' % ('Secant', data_sec[-1][0], data_sec[-1][1])
            print
            sys.exit(1)
        else:
            diff_eval_sec = (f(x_1_copy) - f(x_0_copy)) / float(x_1_copy - x_0_copy)
        f_eval_sec = f(x_1_copy)
        x_0_copy = x_1_copy
        x_1_copy = x_1_copy - f_eval_sec / float(diff_eval_sec)
        data_sec.append((x_1_copy, f_eval))

    print
    print '%20s %20s %20s' % ('Root Finder Type', 'X-approximation', 'Function Value')
    print
    print '%15s %20f %20f' % ('Newton', data[-1][0], data[-1][1])
    print
    print '%15s %20f %20f' % ('Bisector', data_bis[-1][0], data_bis[-1][1])
    print
    print '%15s %20f %20f' % ('Secant', data_sec[-1][0], data_sec[-1][1])
    print
    
if __name__ == '__main__':
    # Map command line arguments to function arguments.
    run(*sys.argv[1:])