#Write a program that uses input to prompt a user for their name and then welcomes them
print("Exercise 1")
print(("Hello ")+input("Enter Name: ").strip()+("!"))

#Write a program to prompt the user for hours and rate per hour to compute gross pay.
print("Exercise 2")
print(("Pay: ") + str(float(input("Enter Hours: ")) * float(input("Enter Rate: "))))

#Write a program which prompts the user for a 
#Celsius temperature, convert the temperature to 
#Fahrenheit, and print out the converted temperature.
print("Exercise 3")

# a = input("Enter Celsius Temperature: ")
# farenheittemp = ( float(a) / 5 ) + 32
# print("Temp: " + str(farenheittemp) + "Degrees Farenheit" )


print("Temp: " + str((9 * float(input("C to F Converter. Enter Celsius Temperature: ").strip()) / 5 ) + 32 ) + " Degrees Farenheit")

# Conditional Execution Exercises
# Rewrite your pay computation to give the 
# employee 1.5 times the hourly rate for hours 
# worked above 40 hours.
# ---- AND
# Rewrite your pay program using try and except so 
# that your program handles non-numeric input 
# gracefully.
print("Exercise 4+5")
try:
	Hours = float(input("Enter Hours: "))
	Rate = float(input("Enter Rate: "))
	if  Hours >= 40:
		print( "Pay: " + str( (40*Rate) + ( (Hours - 40) * (Rate*1.5) ) ) )
	else:
		print( "Pay: " + str(Hours*Rate) )
except ValueError:
	print("Error, please enter numeric input")

#Write a program to prompt for a score between 
#0.0 and 1.0. If the score is out of range or not 
#numeric, print an error message. If the score is 
#between 0.0 and 1.0, print a grade using the 
#following table:
# >= 0. 9 - A ; >= 0.8 - B ; >= 0.7 - C ; >= 0.6 - D ; < 0.6 - F

print("Exercise 6")
try:
	score = float(input("Enter Score: "))
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
except ValueError:
	print("Bad Score/Score is Out of Range.")
