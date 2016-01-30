# coding: utf-8
import math


def sin(x, n):
    sign = 1.0
    sin = 0.0
    for i in range(1, n, 2):
        sin += sign * x ** i / math.factorial(i)
        sign *= -1.0
    return sin

pi = math.pi
v = -pi / 4
print "Sinus med Taylor: "
for i in range(1, 17, 2):
    print i, sin(v, i)
print "math.sin: ", math.sin(v)
