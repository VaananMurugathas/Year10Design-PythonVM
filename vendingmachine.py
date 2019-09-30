import os

kitkatnum = 5
kitkat = 1.50
orangesodanum = 5
orangesoda = 1.25
applenum = 5
apple = 0.50
while True:
	input("Press enter to use vending machine")
	os.system("clear")
	print("1. Kitkat")
	print("2. Orange soda")
	print("3. Apple")
	print(" ")
	option = int(input("Type 1,2 or 3 to choose the option: "))

	if option == 1:
		os.system("clear")
		print("You have selected kitkat")
		if kitkatnum > 0:
			print("There are currently "+str(kitkatnum)+" kitkats left")
			print("The price of a kitkat is "+str(kitkat))
			quantity = int(input("How many kitkats would you like "))
			if quantity > kitkatnum:
				print("Sorry we don't have that many kitkats")
			elif quantity < kitkatnum:	
				kitkatprice = quantity*kitkat
				kitkatnum = kitkatnum - quantity
				print("Your total is "+str(kitkatprice))
				print("Would you like to purchase another option")
				print("1. Apple")
				print("2. Orange soda")
				option2 = int(input("Type 1 or 2 to choose the option: "))
				if option2 == 1:
					os.system("clear")
					if applenum > 0:
						print("There are currently "+str(applenum)+" apples left")
						quantity2 = int(input("How many apples would you like "))
						if quantity2 < applenum:
							appleprice = quantity2*apple
							totalprice = appleprice+kitkatprice
							print("Your total is "+str(totalprice))
							print("Would you like to purchase any orange soda")
							sodayes = int(input("If yes type 1 "))
							if sodayes == 1:
								os.system("clear")
								quantity3 = int(input("how many sodas would you like "))
								if quantity3 > orangesodanum:
									print("Sorry we don't have that many sodas")
								else:
									sodaprice = quantity3*orangesoda
									totalprice = sodaprice+appleprice+kitkatprice
									print("Your total will be "+str(totalprice))

							else:
								print("Sorry we don't have that many sodas available")

							
					elif applenum == 0:
						print("Sorry we are out of apples")

		elif kitkatnum == 0:
			print("Sorry we don't have that option available")
	if option == 2:
		os.system("clear")
		print("You have selected soda")
		if sodanum > 0:
			print("There are currently "+str(sodanum)+" sodas left")
			print("The price of a soda is "+str(soda))
			quantity = int(input("How many sodas would you like "))
			if quantity > sodanum:
				print("Sorry we don't have that many sodas")
			elif quantity < sodanum:	
				sodaprice = quantity*soda
				sodanum = sodanum - quantity
				print("Your total is "+str(sodaprice))
				print("Would you like to purchase another option")
				print("1. Apple")
				print("2. Kitkat")
				option2 = int(input("Type 1 or 2 to choose the option: "))
				if option2 == 1:
					os.system("clear")
					if applenum > 0:
						print("There are currently "+str(applenum)+" apples left")
						quantity2 = int(input("How many apples would you like "))
						if quantity2 < applenum:
							appleprice = quantity2*apple
							totalprice = appleprice+sodaprice
							print("Your total is "+str(totalprice))
							print("Would you like to purchase any kitkat")
							sodayes = int(input("If yes type 1 "))
							if sodayes == 1:
								os.system("clear")
								quantity3 = int(input("how many kitkats would you like "))
								if quantity3 > kitkatnum:
									print("Sorry we don't have that many kitkats")
								else:
									kitkatprice = quantity3*kitkat
									totalprice = sodaprice+appleprice+kitkatprice
									print("Your total will be "+str(totalprice))

							else:
								print("Sorry we don't have that many kitkats available")

							
					elif applenum == 0:
						print("Sorry we are out of apples")

		elif sodanum == 0:
			print("Sorry we don't have that option available")

	if option == 3:
		os.system("clear")
		print("You have selected apple")
		if applenum > 0:
			print("There are currently "+str(applenum)+" apples left")
			print("The price of an apple is "+str(apple))
			quantity = int(input("How many apples would you like "))
			if quantity > applenum:
				print("Sorry we don't have that many apples")
			elif quantity < applenum:	
				appleprice = quantity*apple
				applenum = applenum - quantity
				print("Your total is "+str(appleprice))
				print("Would you like to purchase another option")
				print("1. Kitkats")
				print("2. Orange soda")
				option2 = int(input("Type 1 or 2 to choose the option: "))
				if option2 == 1:
					os.system("clear")
					if kitkatnum > 0:
						print("There are currently "+str(kitkatnum)+" kitkats left")
						quantity2 = int(input("How many kitkats would you like "))
						if quantity2 < kitkatnum:
							kitkatprice = quantity2*kitkat
							totalprice = appleprice+kitkatprice
							print("Your total is "+str(totalprice))
							print("Would you like to purchase any orange soda")
							sodayes = int(input("If yes type 1 "))
							if sodayes == 1:
								os.system("clear")
								quantity3 = int(input("how many sodas would you like "))
								if quantity3 > orangesodanum:
									print("Sorry we don't have that many sodas")
								else:
									sodaprice = quantity3*orangesoda
									totalprice = sodaprice+appleprice+kitkatprice
									print("Your total will be "+str(totalprice))

							else:
								print("Sorry we don't have that many sodas available")

							
					elif applenum == 0:
						print("Sorry we are out of apples")

		elif kitkatnum == 0:
			print("Sorry we don't have that option available")
	else:
		print("Not a valid option")







