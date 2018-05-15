"""
check provided number
"""
import sys

def check_num(num):
    if (num % 15 == 0):
        return "FizzBuzz\n"
    elif (num % 3 == 0):
        return "Fizz\n"
    elif (num % 5 == 0):
        return "Buzz\n"
    else:
        return "%i\n" % (num,)
