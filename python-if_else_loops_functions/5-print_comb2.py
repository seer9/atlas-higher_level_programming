#!/usr/bin/python3
for count in range(100):
    if count < 99:
        print("{:02d}".format(count), end=", ")
    else:
        print("{:02d}".format(count))
