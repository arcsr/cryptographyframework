#!/usr/bin/python

import string
import sys




def main():

	args = sys.argv[1:]
	if(args.__len__() < 5):
		print "Usage rot_cipher.py -s string -r rot# -e|-d\n"	
		sys.exit(1)

	if((args[0] == "-s") and (args[2] == "-r") and (args[4] == "-e")):
		text = args[1] 
		rot = int(args[3])
		to_do = "encode"
	elif((args[0] == "-s") and (args[2] == "-r") and (args[4] == "-d")): 
		text = args[1] 
		rot = int(args[3])
		to_do = "decode"
	else:
		print "Usage rot_cipher.py -s string -r rot# -e|-d\n"	
		sys.exit(1)

	lower = string.ascii_lowercase
	hash1 = {}
	hash2 = {}
	array1 = {}
	array2 = {}
	x = 0
	for l in lower:
		array1[x] = l				
		array2[x] = l				
		x += 1

	#print "array1: %s" % array1
	#print "array2: %s" % array2
	for i in range(0,26):
	#	print "i= %d" % i
		if( (i+rot) <= 25):
			array1[i] = array2[i+rot]		
		else:
			array1[i] = array2[(i+rot)-26]
		hash1[array2[i]] = array1[i]
		hash2[array1[i]] = array2[i]

	text = text.lower()	

		#print "array2: %s" % array2
	#print "array1: %s" % array1
	new_text = ''
	if(to_do == "encode"):
		new_text = encode_string(text,hash1)
	elif(to_do == "decode"):
		new_text = decode_string(text,hash2)
	print new_text

def decode_string(text,ahash):
	returned_string = ''
	for m in text:
		if( m == ' '):
			returned_string += m	
		else:
			returned_string += ahash[m]	

	return returned_string



def encode_string(text,ahash):
	new_string = ''
	for i in text:
		if(i == " "):
			new_string += i	
		else:
			new_string += ahash[i] 		
	
	return new_string

main()
