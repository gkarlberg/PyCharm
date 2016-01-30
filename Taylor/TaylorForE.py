# coding: utf-8
import math


def etaylor(x, n):
    """e calculated using Taylor expansion
    :type x: float
    """
    e = 1.0
    for i in range(1, n):
        e += x ** i / math.factorial(i)
    return e


print "e from Taylor expansion:"
for i in range(1, 16):
    myE = etaylor(1.0, i)
    print str(i), myE

print "The correct e: ", math.e
