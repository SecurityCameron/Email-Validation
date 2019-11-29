import time
import re

valid = False
while valid != True:

	email = input("Enter email: ")

	valid = re.match('[a-zA-Z]+[0-9]*@[a-zA-Z]+',email)

	if valid:
		valid = True
		print ("Valid")

	else:
	    print ("Invalid")


