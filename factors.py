#!/bin/python
num = int(input("enter a positive number to get the factors: "))
for i in range(1, num+1):
    if num%i == 0:
        print(i, end=' ')
