#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    imp = len(sys.argv) - 1

    if imp == 0:
        print("{} arguments.".format(imp))
    elif imp == 1:
        print("{} argument:".format(imp))
    else:
        print("{} arguments:".format(imp))
    if imp >= 1:
        imp = 0
        for args in sys.argv:
            if imp != 0:
                print("{}: {}".format(imp, args))
            imp += 1
