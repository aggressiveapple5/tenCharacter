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
	
lines = f.read().splitlines()
for line in lines:
	if len(line) > 10:
		f.write("no")
	else:
		f.write(line)