#!/usr/bin/env python

import sys
import num_checker

"""
Main funtion
"""
if __name__ == "__main__":
  try:
  end = int(sys.argv[1])
    check_num(end)
  except TypeError:
    sys.stdout.write("Please try with Interger argument\n")
