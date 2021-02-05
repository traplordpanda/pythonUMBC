#!/usr/bin/env python3
""" A Solution For modules_ex02 Part 1
    Create a new file and define a function in it with the same
    name (but different behavior) as one of the functions from
    the previous exercise.
"""

fmt = "Inside of Function: {} of module {}"


def one():
    print(fmt.format(one.__name__, __name__))


def two():
    print(fmt.format(two.__name__, __name__))
