"""
check provided number
"""
import sys

def check_num(num):
    for x in range(1,num+1):
        if (x%15 == 0):
            sys.stdout.write("FizzBuzz\n")
        elif (x%3 == 0):
            sys.stdout.write("Fizz\n")
        elif (x%5 == 0):
            sys.stdout.write("Bazz\n")
        else:
            sys.stdout.write("%i\n" % (x,))

    