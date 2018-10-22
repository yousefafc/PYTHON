#!/usr/bin/python
# listing prime numbers
import sys
var = int(input("prime numbers range from 0 to :"))
var, type(var)
for num in range(2,var):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print(num)

 #task2
