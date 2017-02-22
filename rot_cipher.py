#!/usr/bin/python

import string
import sys
import enchant


word_check = enchant.Dict("en_US")

def main():

	if(sys.argv.__len__() < 3):
		print "Usage rot_cipher.py -s string -r rot# -e|-d\n"	
		sys.exit(1)
	else:
		args = sys.argv[1:]

	if(args.__len__() < 5 and args[2] != "-b"):
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
	elif((args[0] == "-s") and (args[2] == "-b")):
		text = args[1]
		to_do = "bruteforce"
	else:
		print "Usage rot_cipher.py -s string -r rot# -e|-d\n"	
		sys.exit(1)

	lower = string.ascii_lowercase
	hash1 = {}
	hash2 = {}
	array1 = {}
	array2 = {}
	new_text = ''
	x = 0
	for l in lower:
		array1[x] = l				
		array2[x] = l				
		x += 1

	if(to_do == "bruteforce"):
		rot = 0
		for r in range(0,26):
			rot += 1


			for i in range(0,26):
				if( (i+rot) <= 25):
					array1[i] = array2[i+rot]		
				else:
					array1[i] = array2[(i+rot)-26]
				hash2[array1[i]] = array2[i]	
		
			new_text = decode_string(text,hash2)
			words = new_text.split(" ")
			if(word_checker(words) == 1):
				print ("\033[44;33m%s\033[m" % new_text)
			else:
				print new_text
			
	else:

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

def word_checker(words):
	flag = 0
	for w in words:
		if(word_check.check(w)):
			flag = 1
	return flag	

main()
