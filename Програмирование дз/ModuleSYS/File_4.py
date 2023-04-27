import sys
import os

a = list()
for i in sys.argv:
    a.append(i)

os.mkdir(rf"{a[1]}{a[0]}")
