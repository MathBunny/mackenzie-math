import sys
""" The purpose of this program is to ensure that everyone who registered has participated 
	Instructions: Simply write your name and then write your ID # """
num = "-1"
name = ""

def clear():
	print "--------------------------------------------------------------"

def getInput():
	print "Please enter your name:"
	name = str(raw_input())
	if name != "x":
		print "Please enter your unique registration number:"
		num = input()
		print "Thank you " + name + " has successfully registered with #" + num
	else:
		return "x"

def outputArr():
	print "Done"
	
while(True):
	if (getInput() == "x"):
		print "worked"
		outputArr()
		sys.exit()