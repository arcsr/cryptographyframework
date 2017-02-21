#!/usr/bin/python

import sys
import string

args = sys.argv[1:]

lower = string.ascii_lowercase
digits = string.digits
common = lower + digits

def main():

	if(args.__len__() < 3):
		print "Usage morse_code_trans.py -s string -e|-d\n"	
		sys.exit(1)
	
	if((args[0] == "-s") and (args[2] == "-e")):
		text = args[1]
		to_do = "encode"
	elif((args[0] == "-s") and (args[2] == "-d")):
		text = args[1]
		to_do = "decode"	
	else:
		print "Usage morse_code_trans.py -s string -e|-d\n"	
		sys.exit(1)

#	print common

	common_morse = {}
	common_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","-----",".----","..---","...--","....-",".....","-....","--...","---..","----."]
	morse_common = {}
	x = 0
	for i in common:
#		print "%d %s %s" % (x, i, common_code[x]) 
		common_morse[common_code[x]] = i		
		morse_common[i] = common_code[x]
		x += 1

	return_string = ""

	if(to_do == "decode"):
		returned_string = decode_string(text,common_morse)
	elif(to_do == "encode"):
		returned_string = encode_string(text,morse_common)

	print returned_string

def decode_string(text,common_morse):
	new_string = ""
	split_text = text.split(" ")
	for i in split_text:
		if(i in common_morse):
			new_string += common_morse[i]		
		else:
			new_string += " "

	return new_string

def encode_string(text, morse_common):
	new_string = ""
	for i in text:
		if(i in morse_common):
			new_string += morse_common[i]
		else:
			new_string += " "

	return new_string

main()
