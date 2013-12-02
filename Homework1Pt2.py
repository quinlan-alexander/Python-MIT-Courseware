import math

#Name: Quinlan Alexander
#Date: September 28, 2013
#Homework 1

#Exercise 1.7 - Rock, Paper, Scissors

player1 = raw_input ("Choose rock, paper, or scissors: ")
print player1

player2 = raw_input ("Choose rock, paper, or scissors: ")
print player2

if (player1 == 'rock' and player2 == 'scissors'):
	print 'Player 1 wins.'
	
if (player1 == 'rock' and player2 == 'rock'):
	print 'It is a draw.'
	
if (player1 == 'rock' and player2 == 'paper'):
	print 'Player 2 wins.'
	
if (player1 == 'paper' and player2 == 'scissors'):
	print 'Player 2 wins.'
	
if (player1 == 'paper' and player2 == 'paper'):
	print 'It is a draw.'
	
if (player1 == 'paper' and player2 == 'rock'):
	print 'Player 1 wins.'
	
if (player1 == 'scissors' and player2 == 'paper'):
	print 'Player 1 wins.'
	
if (player1 == 'scissors' and player2 == 'scissors'):
	print 'It is a draw.'
	
if (player1 == 'scissors' and player2 == 'rock'):
	print 'Player 2 wins.'


#Exercise 1.8 - for and while loops
#Exercise 1.8 Part 1

for x in range (2,11):
	print (1.0/x)


#Exercise 1.8 Part 2
	
countDown = input ("Choose a number: ")

while (countDown > 0):
	print "Count down: ", countDown
	countDown = countDown - 1


#Exercise 1.8 Part 3

base = input ("Choose a base: ")
exponent = input ("Choose an exponent: ")

print (base ** exponent)


#Exercise 1.8 Part 4

askAgain = True

while(askAgain):
	number1 = input ("Choose a number that is divisible by 2: ")
    
	if number1 % 2 == 0:
		print "Congratulations! The number is divisible by 2."
		askAgain = False
	else:
		print "Choose a number that is divisble by 2"
	
	
