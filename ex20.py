# -*- coding: utf-8 -*-

from sys import argv
import math

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First, let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kinf of like a tape."

rewind(current_file)

print "Let's print three lines:"



'''

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

'''
'''
for current_line in range(1, 5):
    print_a_line(current_line, current_file)
    current_line += 1

'''
current_line = 1
while current_line <= 5:
    print_a_line(current_line, current_file)
    current_line += 1