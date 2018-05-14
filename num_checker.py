"""
check provided number
"""
import sys

def check_num(num):
<<<<<<< HEAD
  for x in range(1,num+1):
    if (x%15 == 0):
      sys.stdout.write("FizzBuzz\n")
    elif (x%3 == 0):
      sys.stdout.write("Fizz\n")
    elif (x%5 == 0):
      sys.stdout.write("Bazz\n")
    else:
      sys.stdout.write("%i\n" % (x,))
=======
    for x in range(1, num):
        if (x % 15 == 0):
            sys.stdout.write("FizzBuzz\n")
        elif (x % 3 == 0):
            sys.stdout.write("Fizz\n")
        elif (x % 5 == 0):
            sys.stdout.write("Bazz\n")
        else:
            sys.stdout.write("%i\n" % (x,))
>>>>>>> 6d74e46da2f09e56b85ca0ceef302229a0e72f9a
