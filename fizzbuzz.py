#!/usr/bin/env python

import sys
from num_checker import check_num

"""
Main funtion
"""
if __name__ == "__main__":
    try:
        end = int(sys.argv[1])
        for x in range(1, end+1):
            sys.stdout.write(check_num(x))
    except ValueError:
        sys.stdout.write("Please try with Interger argument\n")
