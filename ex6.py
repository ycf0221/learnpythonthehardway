# -*- coding: utf-8 -*-

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and whose who %s." %(binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "ISn't that joke so fuuny?! %r"

print joke_evaluation % hilarious

w = "There is the left side of..."
e = "a string with a right side."

print w + e