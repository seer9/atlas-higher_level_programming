#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0

    for num in sys.argv:
        if num != sys.argv[0]:
            sum += int(num)
print(sum)
