#!/usr/bin/python

import sys
import string

args = sys.argv[1:]

lower = string.ascii_lowercase

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

	letters_morse = {}
	letters_code = [".-","-...","-.-.","-..",".","..-.","--.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
	morse_letters = {}
	x = 0
	for i in lower:
		letters_morse[letters_code[x]] = i		
		morse_letters[i] = letters_code[x]
		x += 1


	return_string = ""

	if(to_do == "decode"):
		returned_string = decode_string(text,letters_morse)

	print returned_string

def decode_string(text,letters_morse):
	new_string = ""
	split_text = text.split(" ")
	for i in split_text:
		if(i in letters_morse):
			new_string += letters_morse[i]		
		else:
			new_string += " "

	return new_string


main()
