# Functions

# Rewrite your pay computation with time-and-ahalf for overtime and create a function called 
# computepay which takes two parameters ( hours 
# and rate).

def computepay(Hours = (input("Insert Hours: ")), Rate = (input("Insert Rate: "))):
	Hours = float(Hours)
	Rate = float(Rate)
	if  Hours >= 40:
		print( "Pay: " + str( (40*10) + ( (Hours - 40) * (Rate*1.5) ) ) )
	else:
		print( "Pay: " + str(Hours*Rate) )
try:
	computepay()
except ValueError:
	print("Error, please enter numeric input")

# Rewrite the grade program from 
# the previous chapter using a 
# function called computegrade that 
# takes a score as its parameter and 
# returns a grade as a string.

print("Exercise 2")
def computegrade(score = float(input("Enter Score: "))):
	if 1 < score or score < 0 :
		print("Score is Out of Range.")
	elif score >= 0.9:
		print("Grade: A")
	elif score >= 0.8:
		print("Grade: A")
	elif score >= 0.7:
		print("Grade: A")
	elif score >= 0.6:
		print("Grade: A")
	else:
		print("Grade: F")

try:
	computegrade()
except ValueError:
	print("Bad Score/Score is Out of Range.")

#Loops

# Write a program which repeatedly 
# reads numbers until the user 
# enters "done". Once "done" is 
# entered, print out the total, count, 
# and average of the numbers. If the 
# user enters anything other than a 
# number, detect their mistake using 
# try and except and print an error 
# message and skip to the next 
# number

count = 0
total = 0
maximum = 0
minimum = 0
average = 0

while True:
	try:
		i = (input("Enter a Number: "))
		if i == 'done':
			print("Total: " + str(total) + ", ","Count: " + str(count) + ", ","Maximum: " + str(maximum) + ", ", "Minimum: " + str(minimum) + ", ", "Average: " + str(average) + ".")
			break
		else:
			i = float(i)
		if i >= maximum:
			maximum = int(i) 
		elif minimum == 0:
			minimum = int(i)
		elif i < minimum:
			minimum = int(i)
		count = count + 1
		total = total + int(i)
		average = total/count

	except ValueError:
		print("Error, please enter numeric input")

# Strings

# Write a while loop that starts at the 
# last character in the string and 
# works its way backwards to the 
# first character in the string, printing 
# each letter on a separate line, 
# except backwards.

string = str(input("Enter String: "))
index = len(string) - 1
while index >= 0:
        letter = string[index]
        print(letter)
        index = index - 1

# Write a function called count()
# that accepts a string (word) and a 
# character (char) and outputs the 
# number of occurrences of char in
# word

def compute(word = str(input("Enter Word: ")), char = str(input("Enter Character: ")), count = 0):
	while len(char) != 1: #if input is not one character
		print("Input Invalid. Only enter one character.")
		char = str(input("Enter Character: "))
	for letter in word:
		if letter == char:
			count = count + 1
	print("Number of " + str(char) + " occurences: " + str(count))

compute()

# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475’
# Use find and string slicing to extract the portion of 
# the string after the colon character and then use the 
# float function to convert the extracted string into a 
# floating point number

str = 'X-DSPAM-Confidence: 0.8475'
spconf = str.find(':')  
value = (str[spconf + 1:]).strip()
print(float(value))

# Write a program to read through a file and print the contents of the file 
# (line by line) all in upper case.
# CODE BELOW - For Demonstrative Purposes Only ; Nagccrash sakin teh

# fname = input('Enter the file name:')
# try:
# 	fhand = open(fname)
# except:
# 	print('File cannot be opened:', fname)
# 	exit()

# for line in fhand:
# line = line.rstrip() 
# print(line.upper())

#----

# Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. 
# Count these lines and then compute the total of the spam confidence values from these lines. 
# When you reach the end of the file, print out the average spam confidence.


# Sometimes when programmers get bored or want to have a bit of fun, 
# they add a harmless Easter Egg to their program. 
# Modify the program that prompts the user for the file name so that it prints a 
# funny message when the user types in the exact file name “na na boo boo”. 
# The program should behave normally for all other files which exist and don’t exist. 
# Here is a sample execution of the program:

fname = input('Enter the file name:')
count = 0
total = 0
if fname == 'stan loona':
    print('taste')
try:
    fhand = open(fname.strip())
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence: '):
        spconf = line.find(':')
        value = (line[spconf + 1:]).strip()
        count = count + 1
        total = total + float(value)
    else:
        continue

print('Average Spam Confidence: ', total/count)