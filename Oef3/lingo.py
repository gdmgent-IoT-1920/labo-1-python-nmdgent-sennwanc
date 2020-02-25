import random
# creating random number
rnumb = random.randrange(1000, 9999)
print(rnumb)

# cast the number to string
rnumb = str(rnumb)
print(rnumb[0])

# ask for user input
inpUser = input("Welkom bij LINGO, geef 4 cijfers in aub ! : " )
print(inpUser)

# compare user input to rnumb
eiCounter = 0
kipCounter = 0
if inpUser == rnumb : 
	print("Proficiat je hebt gewonnen !")
else:
	i = 0
	for x in rnumb :
		if x == inpUser[i]: 
			print("Je hebt een kip")
			kipCounter += 1
		elif x in inpUser: 
			print("Je hebt een ei'tje")
			eiCounter += 1
		else: 
			print("Je hebt geen goede cijfers")

		i += 1

print("Je hebt {0} x kip en {1} x ei".format(kipCounter, eiCounter))
