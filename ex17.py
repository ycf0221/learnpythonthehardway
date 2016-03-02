# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copy from %s to %s" % (from_file, to_file)

# We coule do these two on one line, how?
#in_file =  open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

print "The input file is %d bytes long." % len(indata)

print "Does the output file exist?%r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("???")

out_file = open(to_file, 'w')
out_file.write(indata)

#只有在out_file.close()之后，才能在下面打印出to_file的内容。否则无法打开。
#猜测：如果out_file一直打开，参数为‘w’,和接下来的read有冲突，所以需要关闭然后重新打开。
out_file.close()    




print "Does the output file exist?%r" % exists(to_file)

print "Alright, all done."


print "from_file:\n", open(from_file).read()
print "to_file:\n", open(to_file).read()

