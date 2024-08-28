#!/usr/bin/python3
def uppercase(str):
  for char in str:
    if ord('a') <= ord(char) <= ord('z'):
      char = chr(ord(char) + (ord('A') - ord('a')))
    print("{}".format(char), end="")
  print()


uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")