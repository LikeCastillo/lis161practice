# --- LISTS ---



# Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None. Then write 
# a function called middle that takes a list and returns a new list that 
# contains all but the first and last elements

mylist = []
choppedlist = []
middlelist = []

def chop(mylist):
	del mylist[0]
	del mylist[-1]
	return None

def middle(mylist):
	middlelist = middlelist + mylist[0] + mylist[-1]
	return middlelist


while True:
	myword = str(input("Add things to your list, type ListDone if you're done: "))
	if myword == "ListDone":
		print("Here is your full list: ",mylist)
		break
	else:
		mylist.append(myword)	
		print(mylist)


while True:
	decision = str(input("Chop, Middle, or Display? "))
	if decision == "Chop" or "chop":
		chop(mylist)
		print("Here is your full list: ", mylist)
		break
	elif decision == "Middle" or "middle": 
		middle(mylist)
		print("Here is your full list: ", middlelist)
		break
	elif decision == "Display" or "display": 
		print("Here is your full list: ", mylist)
		break
	else:
		print("Invalid Decision.")


# Download a copy of the file www.py4e.com/code3/romeo.txt. Write 
# a program to open the file romeo.txt and read it line by line. For 
# each line, split the line into a list of words using the split function. 
# For each word, check to see if the word is already in a list. If the 
# word is not in the list, add it to the list. When the program 
# completes, sort and print the resulting words in alphabetical order.

fulllist = []

def openromeo(fhand):
	for line in fhand:
		line = line.rstrip()
		line = line.split()
		for word in line:
			if str(word) in fulllist:
				continue
			else:
				fulllist.append(word)
	
	fulllist.sort()
	return fulllist
fname = input('Enter the file name:')

if fname == 'romeo.txt':
	fhand = open(fname.strip())
	print("works")
	openromeo(fhand)
	print(fulllist)

# Write a program to read through the mail box data and when you 
# find line that starts with "From", you will split the line into words 
# using the split function. We are interested in who sent the 
# message, which is the second word on the From line.
# You will parse the From line and print out the second word for 
# each From line, then you will also count the number of From (not 
# From:) lines and print out a count at the end. This is a good 
# sample output with a few lines removed:


fname = input('Enter the file name:')
count = 0
if fname == 'stan loona':
    print('taste')
try:
    fhand = open(fname.strip())
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word.")



# --- DICTIONARIES ---



# Write a program that reads the words in words.txt 
# and stores them as keys in a dictionary. 
# It doesn’t matter what the values are. Then you can use the 
# in operator as a fast way to check whether a 
# string is in the dictionary.


fname = input('Enter the file name:')
count = 0
dictionary = {}

if fname == 'stan loona':
    print('taste')
try:
    fhand = open(fname.strip())
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
	words = line.split()

	for word in words:
		if (word not in dictionary.keys()):
			dictionary[word] = count
			count = count + 1
		else:
			continue


print(dictionary)


# Write a program that categorizes each mail message by which day of the week 
# the commit was done. To do this look for lines that start with "From", then look 
# for the third word and keep a running count of each of the days of the week. At 
# the end of the program print out the contents of your dictionary (order does not 
# matter).

fname = input('Enter the file name:')
count = 0
dictionary = {}

if fname == 'stan loona':
    print('taste')
try:
    fhand = open(fname.strip())
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
	words = line.split()

	for word in words:
		if (word not in dictionary.keys()):
			dictionary[word] = count
			count = count + 1
		else:
			continue


print(dictionary)

# Write a program that categorizes each mail message by which day of the week 
# the commit was done. To do this look for lines that start with "From", then look 
# for the third word and keep a running count of each of the days of the week. At 
# the end of the program print out the contents of your dictionary (order does not 
# matter).

fname = input('Enter the file name:')
count = 0
d = dict()

if fname == 'stan loona':
    print('taste')
try:
    fhand = open(fname.strip())
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    day = words[2]
    if day not in d:
    	d[day] = 1
    else:
    	d[day] = d[day] + 1

print(d)

# Write a program to read through a mail log, build a histogram using a 
# dictionary to count how many messages have come from each email address, 
# and print the dictionary

fname = input('Enter the file name:')
count = 0
d = dict()

if fname == 'stan loona':
    print('taste')
try:
    fhand = open(fname.strip())
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    if email not in d:
    	d[email] = 1
    else:
    	d[email] = d[email] + 1

print(d)


# Add code to the above program to figure out who has the most messages in 
# the file. After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop to find who has the most 
# messages and print how many messages the person has.


fname = input('Enter the file name:')
count = 0
d = dict()

if fname == 'stan loona':
    print('taste')
try:
    fhand = open(fname.strip())
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    if email not in d:
    	d[email] = 1
    else:
    	d[email] = d[email] + 1

largest = 0
maxkey = None
for key, value in d.items():
	if value is None or value > largest:
		largest = value
		maxkey = key

print(maxkey, largest)


# This program records the domain name (instead of the address) where the 
# message was sent from instead of who the mail came from (i.e., the whole 
# email address). At the end of the program, print out the contents of your 
# dictionary


fname = input('Enter the file name:')
count = 0
d = dict()

if fname == 'stan loona':
    print('taste')
try:
    fhand = open(fname.strip())
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    if pieces[1] not in d:
    	d[pieces[1]] = 1
    else:
    	d[pieces[1]] = d[pieces[1]] + 1

print(d)



# --- TUPLES ---

# Exercise 1: Revise a previous program as follows: Read and parse the “From” 
# lines and pull out the addresses from the line. Count the number of messages from
# each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a 
# list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has the most commits.

import string
fname = input('Enter the file name:')
count = 0
d = dict()

if fname == 'stan loona':
    print('taste')
try:
    fhand = open(fname.strip())
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    if email not in d:
    	d[email] = 1
    else:
    	d[email] = d[email] + 1

lst = list()
for key,val in list(d.items()):
	lst.append((val, key))

lst.sort(reverse = True)

for key, val in lst[:1]:
    print(val, key)

# Exercise 2: This program counts the distribution of the hour of the day for
# each of the messages. You can pull the hour from the “From” line by finding the
# time string and then splitting that string into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts, one per line,
# sorted by hour as shown below.


import string
fname = input('Enter the file name:')
count = 0
d = dict()

if fname == 'stan loona':
    print('taste')
try:
    fhand = open(fname.strip())
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    time = words[5]
    time = time.split(":")
    time = time[0]
    if time not in d:
    	d[time] = 1
    else:
    	d[time] = d[time] + 1

lst = list()
for key,val in list(d.items()):
	lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
