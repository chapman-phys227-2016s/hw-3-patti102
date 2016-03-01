#! /usr/bin/env python

"""
File: loan.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module calculates the arclength of argument functions with the classical arclength
function taken over descrete integration. The integration of an erg function is also shown as
an example.

"""


import numpy as np

def der_numerical(f, h=1e-5):
    """Provides numerical integrals for argument functions."""
    return lambda x: ((f(x + h) - f(x - h)) / (2 * h))

def arclength(f, a, b, n):
    """Calculates the arclength with the typical formula taken over descrete integration."""
    increment = (b - a) / float(n)
    curve_length = np.zeros(n+1)
    curve_length[0] = 0
    der_f = der_numerical(f)
    for n in range(1, n+1):
        derrivative = der_f(a + n * increment)
        curve_length[n] = curve_length[n - 1] + np.sqrt(1 + np.abs(derrivative)**2) * increment
    return curve_length

def part_c(x):
    """An Erg function is defined so that its arclength might be taken as an example."""
    increment = (x + 2) / float(1000)
    integral = 0
    for n in range(1001):
        integral = integral + np.exp(-4 * (-2 + n * increment)**2) * increment
    integral = integral / np.sqrt(2 * np.pi)
    return integral

def test_quarter_circle():
    """Ensures that the function integrates accurately for the arclength of a quarter circle."""
    def quarter_circle(x):
        return np.sqrt(1.0001 - x**2)
    apt = np.abs(arclength(quarter_circle, 0, 1, 100000)[-1] - (np.pi / 2)) < 1e-2
    msg = "The arclength obtained was not of the length of a quarter circle pi over 2"
    assert apt, msg