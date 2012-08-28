#!/usr/bin/env python
# coding: utf-8

##########################
## Author: opnchaudhary ##
##########################
import os
import re
import sys

def grab_fileNames(file):
	"""This should extract all the files  with .m extension."""
	#This is the email address pattern in ReGex
	fileName_pattern = re.compile(r'\b[A-Za-z0-9]+[.][m]\b',re.IGNORECASE)

	found = set()
	if os.path.isfile(file):
		for line in open(file, 'r'):
			found.update(fileName_pattern.findall(line))
		for filenames in found:
			print filenames
if __name__ == '__main__':
	grab_fileNames(sys.argv[1])
