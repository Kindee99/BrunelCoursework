weapons = ["sword", "dagger"]
fightMode = False

while True:

	usr=input("Where to? ")
	if usr in ['s', "south"] or usr in ["w", "west"] or usr in ["e", "east"]:
		print("Nothing there")
	elif usr in ["n", "north"]:
		print("Oh this looks like trouble!")

		 
		usr = input("Will you fight?").lower()
		if usr in ["yes", "y", "hell yeah"]:
			fightMode = True
		else:
			continue


		while fightMode:

				usr = input("which weapon you want to use: ")

				usrp = usr.split(" ") #list
	  
				for word in usrp:
					if word in weapons:
						if word == "sword":
							print("With this you do 5 damage. On we go!")
							fightMode = False
						 
					elif word == "dagger":
							print("With this you do 3 damage. On we go!")
							fightMode = False
						 
					else:
						print("please choose a weapon you actually have")

		# Further code for the fight ...
 
	else:
		print("That's not a valid direction")
