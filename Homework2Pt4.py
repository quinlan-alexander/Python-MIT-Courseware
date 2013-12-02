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


def nims():
	numberOfStones=100
	turn = 1
	player1Again = True;
	while numberOfStones > 5:
		while True:
			playerstones = input("How many stones will Player" + str(turn) + " take from the pile? ");
			if (playerstones >= 1 and playerstones <= 5):
				break
				
		numberOfStones = numberOfStones - playerstones;
		print "There are " + str(numberOfStones) + " stones left";
		if turn == 1:
			turn = 2;
		else:
			turn = 1;
	if turn == 1:
		print "Player 1 wins!";
	else:
		print "Player 2 wins!";
		
#nims()


def report_card():
	classes = input("How many classes are you taking?: ")
	total_grade = 0;
	index = classes;
	while index > 0:
		name = raw_input("What is the name of the class: ");
		grade = input("What score did you get in that class?: ");
		total_grade = total_grade + grade;
		print name + " - " + str(grade);
		index = index - 1;
	average = float(total_grade/classes)
	print "Overall Average - " + str(average);
	
#report_card()


def sum_all(number_list):
    total = 0
    for num in number_list:
        total += num

    return total

print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
	i = 0
	sum = 0
	
	#sum_list = [len(number_list)]
	#sum_list = list(len(number_list)
	
	sum_list = []
	
	i = 0
	
	while i < len(number_list):
		number = number_list[i];
		sum += number;    
		i = i + 1;
		sum_list.append(sum);
		
	print "Printing the cumulative sum in a form of a list: " + str(sum_list)	

cumulative_sum([1, 2, 3, 4, 5])	
		

def pig_latin():
	vowels = ["a", "e", "i", "o", "u"]
	word = raw_input("What is your word?: ")
	first_char = word[0]
	if first_char in vowels:
		print str(word) + "hay"
	else:
		print word[1:len(word)] + first_char + "ay"
	
	
pig_latin()
		