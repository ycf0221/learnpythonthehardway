# -*- coding: utf-8 -*-

my_name = "Yu changfu"
my_age = 33
my_height = 74
my_weight = 130
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'
a1 = 1.773
a2 = 1.222


print "a1", round(a1)
print "a2", round(a2)
print "Let's talk about %s" % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print " His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)