# crackle_pop

#INSTRUCTIONS:
#Write a program that prints out the numbers 1 to 100 (inclusive). 
#If the number is divisible by 3, print Crackle instead of the number.
#If it's divisible by 5, print Pop.
#If it's divisible by both 3 and 5, print CracklePop. 

#first commit

def crackle_pop(i):
	while (i >= 1 and i <= 100):
		if (i % 3 == 0):
			print("Crackle")
		elif (i % 5 == 0):
			print("Pop")
		elif (i % 3 == 0 and i % 5 == 0):
			print("CracklePop")
		else:
			print(i)
	#i += 1

crackle_pop(1)


#if bugged: consider a for loop instead 