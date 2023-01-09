"""Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59"""


def past(h, m, s):
    ml = 0
    while h > 0 or m > 0 or s > 0:
        if h > 0:
            ml += 3600000
            h -= 1
        if m > 0:
            ml += 60000
            m -= 1
        if s > 0:
            ml += 1000
            s -= 1
    return ml
