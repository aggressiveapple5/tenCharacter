#Author: Matt Keller
#Date: March 3, 2016
import os

file = raw_input("What file would you like to open? ")

if os.path.isfile(file):
	f = open(file, 'r+')
else:
	f = open(file, 'w')
	f.close()
	f = open(file, 'r+')
secondFile = raw_input("What file would you like to print to?")

h = open(secondFile, 'w')

	
lines = f.read().splitlines()
for line in lines:
	if len(line) > 10:
		h.write(line[:10])
	else:
		h.write(line)
	h.write("\n")
	
		