import random
Money = 1000

while money > 0:
	bet = int(input("How much are you betting this round? \n"))
	c1 = random.randint(1,15)
	if c1 == 15:
		c1 = 11
	elif c1 >= 10 and c1 < 15:
		c1 = 10
	print(c1)
	print("If you want to hit type 1 \nIf you want to stay type 0")
	hit = int(input("Would you like to hit or stay? \n"))
	if hit == 1:
		c2 = random.randint(1,11)
		print(c2)
		total = int(c1) + int(c2)
		if total > 21:
			print("You went bust!")
			money = money - bet
			print("You have " + money + "dollars left")
		elif total < 21:
			print("If you want to hit type 1 \nIf you want to stay type 0")


