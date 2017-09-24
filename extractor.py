#!/usr/bin/env python
# coding: utf-8

import os
import re
import sys

def grab_email(file):
	# Try and grab all emails addresses found within a given file.
	#This is the email address pattern in ReGex
	email_pattern = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b',re.IGNORECASE)

	found = set()
	if os.path.isfile(file):
		for line in open(file, 'r'):
			found.update(email_pattern.findall(line))
		for email_address in found:
			print email_address

if __name__ == '__main__':grab_email(sys.argv[1])
