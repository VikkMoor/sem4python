"""Calculate a number with a given precision"""
from math import pi

d = int(input("Enter a value of precision for calculate Pi: "))
print(f'Pi with a precision of {d} is {round(pi, d)}')
