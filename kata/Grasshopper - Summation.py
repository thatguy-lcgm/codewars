"""Write a program that finds the summation of every number from 1 to num.
The number will always be a positive integer greater than 0."""


def summation(num):
    n = 0
    for c in range(1, num + 1):
        n += c
    return n


print(summation(8), '\033[33m36\033[m')
