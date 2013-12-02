import math
import random

def rockPaperScissors(player1, player2):
	if (player1 == 'rock' and
		player2 == 'scissors'):
		print 'Player 1 wins.'
	
	if (player1 == 'rock' and
		player2 == 'rock'):
		print 'It is a draw.'
	
	if (player1 == 'rock' and
		player2 == 'paper'):
		print 'Player 2 wins.'
	
	if (player1 == 'paper' and
		player2 == 'scissors'):
		print 'Player 2 wins.'
	
	if (player1 == 'paper' and
		player2 == 'paper'):
		print 'It is a draw.'
	
	if (player1 == 'paper' and
		player2 == 'rock'):
		print 'Player 1 wins.'
	
	if (player1 == 'scissors' and
		player2 == 'paper'):
		print 'Player 1 wins.'
	
	if (player1 == 'scissors' and
		player2 == 'scissors'):
		print 'It is a draw.'
	
	if (player1 == 'scissors' and
		player2 == 'rock'):
		print 'Player 2 wins.'
		
print rockPaperScissors('rock', 'scissors')

def is_divisible(m, n):
	if m % n == 0:
		return True
	else:
		return False
		
print is_divisible(10, 2)
print is_divisible(18, 7)
#print is_divisible(42, 0)

def not_equal(number1, number2):
	if number1 == number2:
		return True
	else:
		return False
		
print not_equal(1, 2)

def multadd(a, b, c):
	print a*b+c


def rand_divis_3():
	x = random.randint(0, 100)
	print x
	if x % 3 == 0:
		return True
	else:
		return False
		
print rand_divis_3()

def roll_dice(side, dice):
	while dice >= 1:
		s = random.randint(1, side);
		print s;
		dice = dice - 1
		
	print "That's all!"
	
roll_dice(4, 5)

def roots(a, b, c):
	x = ((b**2)-(4*a*c))**0.5;
	x = -b+((b**2)-(4*a*c))**0.5;
	x = (-b+((b**2)-(4*a*c))**0.5)/(2.0*a);
	print x;
	y = ((b**2)-(4*a*c))**0.5;
	y = -b-((b**2)-(4*a*c))**0.5;
	y = (-b-((b**2)-(4*a*c))**0.5)/(2.0*a);
	print y;
			
roots(1, 10, 2)


    #def nims(pile, max_stones):
	#game_over=false
	#player_turn=1
	#while (!game_over):
	#	print "player "+player_turn
	#	do:
	#		player = input("Choose a number that is between 1 to :"+max_stones)
	#	while ((player > 0) and (player <= max_stones))
    #   pile=pile-player
    #	print pile
    	
    #	if (pile == 0):
    #		print "player "+player_turn+" wins!"
    #		game_over=true
    	
    #	player_turn=2

#end
#end
    
#nims(100, 5)


			