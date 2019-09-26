import random
import os


money = 3000

while money > 0:
	house = random.randint(14,21)
	print("You have " + str(money)+" dollars left")
	bet = int(input("How much are you betting this round? \n"))
	c1 = random.randint(1,15)
	if c1 == 15:
		c1 = 11
	elif c1 >= 10 and c1 < 15:
		c1 = 10
	print("Your card is "+str(c1))
	print("If you want to hit type 1 \nIf you want to stay type 0")
	hit = int(input("Would you like to hit or stay? \n"))
	if hit == 1:
		c2 = random.randint(1,15)
		if c2 == 15:
			c2 = 11
		elif c2 >= 10 and c2 < 15:
			c2 = 10
		print("Your card is "+str(c2))
		total = int(c1) + int(c2)
		if total > 21:
			print("You went bust!")
			money = money - bet
			print("You have " + str(money) + "dollars left")
		elif total < 21:
			print("If you want to hit type 1 \nIf you want to stay type 0")
			hit2 = int(input("Would you like to hit or stay \n"))
			if hit2 == 1:
				c3 = random.randint(1,15)
				if c3 == 15:
					c3 = 11
				elif c3 >= 10 and c3 < 15:
					c3 = 10
				print("Your card is "+str(c3))
				total = int(c1) + int(c2) + int(c3)
				print("The house's total is "+str(house))
				if total > 21:
					print("You went bust!")
					money = money - bet
					# print("You have " + str(money) + " dollars left")
				elif total < 22:
					print("You must stay this round")
					if house >= total:
						print("You lost")
						money = money - bet
						# print("You have " + str(money) + " dollars left")
					else:
						print("You won!")
						money = money + bet
						# print("You now have " + str(money) + " dollars left")
			elif hit2 == 0:
				print("The house's total is "+str(house))
				if total <= house:
					money = money - bet
				else:
					print("You won!")
					money = money + bet
					# print("You now have " + str(money) + " dollars left")
	elif hit == 0:
		if c1 > 21:
			print("You went bust!")
			money = money - bet
			# print("You have " + str(money) + " dollars left")
		elif c1 < 22:
			house2 = random.randint(10,21)
			print("The house's total is "+str(house2))
			if house2 >= c1:
				print("You lost")
				money = money - bet
				# print("You have "+str(money)+" dollars left")
			else:
				print("You won!")
				money = money + bet
				# print("You have "+str(money)+" dollars left")
	lmao = input("Type next to proceed to the next round ")
	os.system('clear')

print("You will never beat the system")




