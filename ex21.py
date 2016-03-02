# -*- coding: utf-8 -*-

def add(a, b):
    print "ADDING %r + %r" % (a, b)
    return float(a + b)

def subtrack(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

#age = add(30, 5)
add_a = float(raw_input("add_a:"))
add_b = float(raw_input("add_b:"))
age = add(add_a, add_b)
height = subtrack(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtrack(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"