#!/usr/bin/python

import string
import sys

lower = string.ascii_lowercase
freq_hash = {}
freq_string = {}
precent = [8.2,1.5,2.8,4.3,12.7,2.2,2.0,6.1,7.0,0.2,0.8,4.0,2.4,6.7,7.5,1.9,0.1,6.0,6.3,9.1,2.8,1.0,2.4,0.2,2.0,0.1]
x = 0
for i in lower:
	freq_hash[i] = precent[x]
	freq_string[i] = 0
	x += 1
	
print freq_hash

args = sys.argv[1:]

if(args.__len__() < 2):
	print "Usage frequency.py -s string"
if(args[0] == '-s'):
	encoded_string = args[1]	


encoded_string = encoded_string.lower()
for enc_str in encoded_string:
	if( enc_str == ' '):
		next
	else:
		freq_string[enc_str] += 1

print freq_string

