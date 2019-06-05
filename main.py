print("""Photopollution Calculator Copyright (C) 2019  Conor Casey
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions. For further details, type `license'.

Don't know how to use the program? Type "help" for support.
To get a history of the updates released for this program, type "updates"
To exit the program, type 'quit'.

Current Edition: v4.0.0""")

def main():
	import pandas as pd
	import math

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
		pd_filename = 'Data/Population_Density/population_density_combined.csv'
		pd_data = pd.read_csv(pd_filename)
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
	sqm = -2.51632097e-03 * user_input + 2.07271443e+01

	#Understanding LUX Values
	def conditions():
		if sqm > 21:
			return " Excellent Stargazing Conditions"
		elif sqm > 20:
			return " Great Stargazing Conditions"
		elif sqm > 19:
			return " Good Stargazing Conditions"
		elif sqm > 18:
			return " Fair Stargazing Conditions"
		elif sqm > 17:
			return " Poor Stargazing Conditions"
		elif sqm < 17:
			return " Terrible Stargazing Conditions"			

	#Result/Output
	print("""
Photopollution in this location is approximately """ + str(round(sqm, 2)) + " mags / arcsec^2, this" + """
should correlate to""" + conditions())

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