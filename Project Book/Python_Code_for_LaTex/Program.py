print """Photopollution Calculator Copyright (C) 2018  Conor Casey
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions. For further details, type `license'.

Don't know how to use the program? Type "help" for support.
To exit the program, type 'quit'.

Updates:
v0.1.0: Initial beta version based on the mathematical model from the SciFest
project called "How Population Density Influences Light Pollution".
v0.1.1: Allowed population density figures to be inputted.
v0.5.0: The mathematical model is updated, and is now based on the 
BT Young Scientist project called "Is it Possible to Create a Mathematical Model
to Predict Photopollution Based on Population Density in Munster".
v0.5.1: Includes licensing agreement.
v0.5.2: Updated population density figures to include the figures from the 
2016 Census.
v0.5.3: See those bugs, no? Well, they are gone!
v0.5.4: Slight changes to the mathematical model.
v0.6.0: Slight changes to the grading system and mathematical model.
v0.6.1: Fixed TypeError when entering a text value for population density.
v0.6.2: See those bugs, no? Well, they are gone!
v0.6.3: Updated to support Windows and macOS alongside Linux.
v1.0.0: Worldwide Public Release on Github!
v1.0.1: Day 1 Bug Patch.
v1.1.0: Let's Get Py Crazy! update.
v1.1.1: Small Changes and Fixes
v1.2.0: Major Changes to Data Calculations
v1.5.0: Fin 2018 update
v1.5.1: Emergency Bug Fix Update
v1.5.2: Small Changes and Fixes
v1.6.0: Errer Update

Current Edition: v1.5.2"""

def main():
	#Imports Population Density Data from the Central Statistics Office
	import pandas as pd
	import math
	pd_filename = 'Data/Population_Density/populationdensitycensustowns.csv'
	pd_data = pd.read_csv(pd_filename)

	place_town = raw_input("""
Is the name of the town being entered: """).lower()
	
	#Licensing Agreement
	if place_town == "license":
		license = open('Help and Licensing Agreement/license.txt','r')
		license_read = license.read()
		print license_read
		license.close()
		main()
	#Force Closes Application	
	elif place_town == "quit":
		quit()
	elif place_town == "help":
		text = open('Help and Licensing Agreement/help.txt','r')
		text_read = text.read()
		print text_read
		text.close()
		main()					
	
	#Population Density or Town Input
	elif place_town == "no":
		place = raw_input("""
Enter the Population Density: """)
		if place.isdigit() == False:
			print "It appears you have entered words instead of numbers, please try again."
			main()
		else:
			print place
			user_input = float(place)
			
	#If A Town Is Entered
	elif place_town == "yes":	
		towns = raw_input("""
Please input the name of the town: """).title()
		town = pd_data[pd_data.Towns.isin([towns])]
		town.reset_index(inplace = True, drop = True)	
		print town 
		user_input = float(town.PD)
		if not town.empty: 
			print town 
			user_input = float(town.PD)
		else:
			print "No population density data for the town of " + towns + " is available."
			main()
	else:
		print "Invalid Entry"
		main()	

	#Calculation of Light Pollution 		
	lux = 0.03510566 * user_input - 14.32414198

	#Get Limerick's Population Density In Order to Understand what the LUX Values Mean 
	limerick = pd_data[pd_data.Towns.isin(["Limerick City"])]
	limerick.reset_index(inplace = True, drop = True)
	limerick_pd = float(limerick.PD)
	limerick_lux = 0.03510566 * (limerick_pd) - 14.32414198

	#Understanding LUX Values
	calculations = (lux) / (limerick_lux) * 100
	def conditions():
		if calculations >= 80:
			return " Terrible Stargazing Conditions"
		elif calculations >= 60:
			return " Poor Stargazing Conditions"
		elif calculations >= 40:
			return " Fair Stargazing Conditions"
		elif calculations >= 20:
			return " Good Stargazing Conditions"
		elif calculations >= 0:
			return " Excellent Stargazing Conditions"			

	#Result/Output
	if calculations >= 0:
		print """
Photopollution in this location is approximately """ + str(int(math.ceil(lux))) + " LUX, this should" + """
correlate to""" + conditions()
	elif calculations < 0:
		print """
Oops, it appears we are getting a negative LUX value. Your population density
is extremely low, therefore, this correlates to Excellent Stargazing Conditions."""

	#Restarts Program
	restart = raw_input("""
Do You Want to Restart the Program: """).lower()
	if restart == "yes":
		print """
		Restarting..."""
		main()
	else:
		quit()	
main()