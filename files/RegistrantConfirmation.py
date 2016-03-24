import sys
from array import array
""" The purpose of this program is to ensure that everyone who registered has participated 
	Instructions: Simply write your name and then write your ID # """

names = []
numbers = []
names.append('Horatiu')
numbers.append(0)
num = "-1"
name = ""

#Clear the screen
def clear():
	print "--------------------------------------------------------------"

#Get the input from the user. x means stop!
def getInput():
	print "Please enter your name:",
	name = str(raw_input())
	if name != "x":
		print "Please enter your unique registration number:",
		try:
			num = input()
		except (RuntimeError, TypeError, NameError):
			print "Error: Enter a valid number."
			getInput()
			return ""
		print "Thank you,",
		print name,
		print "has successfully registered with #",
		print num
		names.append(name)
		try:
			numbers.append(num)
		except (RuntimeError, TypeError, NameError):
			print "Error: Enter a number."
			getInput()
			
		clear()
		return ""
	else:
		return "x"

#Output the final array of numbers and words
def outputArr():
	file = open("contest.txt", "w")
	file.write("Math Contest Registration Confirmation System:\n")
	for x in range (len(names)):
		file.write(names[x])
		file.write(" ")
		file.write(str(numbers[x]))
		file.write("\n")
	file.close()

#This is the main program	
while(True):
	if (getInput() == "x"):
		print "Done!"
		outputArr()
		sys.exit()