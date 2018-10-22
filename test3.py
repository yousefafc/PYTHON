#!/usr/bin/python
from functools import partial
#normal function

def sumOf(a, b):
    return(a+b)
print(sumOf(1, 2))

#partial
plusTwo = partial(sumOf, 2)
print(plusTwo(1))