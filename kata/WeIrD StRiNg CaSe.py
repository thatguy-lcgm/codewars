"""
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns
the same string with all even indexed characters in each word upper cased, and all
odd indexed characters in each word lower cased. The indexing just explained is zero
based, so the zero-ith index is even, therefore that character should be upper cased
and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' ').
Spaces will only be present if there are multiple words. Words will be separated by
a single space(' ').
https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python
"""


def to_weird_case(words):
    re = ''
    inv = 1
    for letter in words:
        if letter == ' ':
            re += ' '
            if inv < 1:
                inv += 1
            continue
        elif inv == 1:
            re += letter.upper()
            inv -= 1
        else:
            re += letter.lower()
            inv += 1
    return re
