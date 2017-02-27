#!/usr/bin/python

import string
import sys

lower = string.ascii_lowercase


enciphered = []
key = 3

lower_array = list(lower)

print lower_array
flag = 0
while lower_array:
	x = 0 
	for j in lower_array:
		if(x % key == 0 and flag == 1):
			enciphered.append(j)
			lower_array.remove(j)
		flag = 1
		x += 1


print enciphered
		

