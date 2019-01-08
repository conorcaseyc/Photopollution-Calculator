print("""Photopollution Calculator Copyright (C) 2018  Conor Casey
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions. For further details, type `license'.

Don't know how to use the program? Type "help" for support.
To get a history of the updates released for this program, type "updates"
To exit the program, type 'quit'.

Current Edition: v2.0.0""")

def main():
	#Imports Population Density Data from the Central Statistics Office
	import pandas as pd
	import math
	pd_filename = 'Data/Population_Density/populationdensitycensustowns.csv'
	pd_data = pd.read_csv(pd_filename)

	place_town = input("""
Is the name of the town being entered: """).lower()
	
	#Updates
	if place_town == "updates":
		updates = open('UPDATES.md', 'r')
		updates_read = updates.read()
		print (updates_read)
		updates.close()
		main()
	#Licensing Agreement
	if place_town == "license":
		license = open('LICENSE','r')
		license_read = license.read()
		print(license_read)
		license.close()
		main()
	#Help Section
	elif place_town == "help":
		text = open('README.md','r')
		text_read = text.read()
		print(text_read)
		text.close()
		main()
	#Force Closes Application	
	elif place_town == "quit":
		quit()				
	
	#Population Density or Town Input
	elif place_town == "no":
		place = input("""
Enter the Population Density: """)
		if place.isdigit() == False:
			print("It appears you have entered words instead of numbers, please try again.")
			main()
		else:
			print(place)
			user_input = float(place)
			
	#If A Town Is Entered
	elif place_town == "yes":	
		towns = input("""
Please input the name of the town: """).title()
		town = pd_data[pd_data.Towns.isin([towns])]
		town.reset_index(inplace = True, drop = True)	
		if not town.empty: 
			print (town) 
			user_input = float(town.PD)
		else:
			print ("No population density data for the town of "), (towns), (" is available.")
			main()
	else:
		print("Invalid Entry")
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
		print("""
Photopollution in this location is approximately """ + str(int(math.ceil(lux))) + " LUX, this should" + """
correlate to""" + conditions())
	elif calculations < 0:
		print("""
Oops, it appears we are getting a negative LUX value. Your population density
is extremely low, therefore, this correlates to Excellent Stargazing Conditions.""")

	#Restarts Program
	restart = input("""
Do You Want to Restart the Program: """).lower()
	if restart == "yes":
		print("""
		Restarting...""")
		main()
	else:
		quit()	
main()

#End of Code
