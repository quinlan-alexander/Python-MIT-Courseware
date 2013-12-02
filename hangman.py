import random

def print_word(word):
	for i in range(len(word)):	
		print word[i],

def correct_guess(word1, word2):
	return word1 == ''.join(map(str,word2))	

def hangman():
	max_guesses = 6
	secret_word = ["less", "cat", "dog", "rock", "plant", "flower", "turkey", "computer", "cranberries", "grass"]
	x = random.randint(0, 7)
	random_word = secret_word[x]
	
	guesses = []
	for i in range(len(random_word)):
 		guesses.append('_')
	
	print_word(guesses)
	
	i = 0
	while i < len(random_word):
		guesses[i] = "_"
		i = i + 1
	
	print
	print
    
	while max_guesses > 0:
		letter = raw_input("Guess a letter: ")
		position = random_word.find(letter);
		
		if position >= 0:
			i = 0
			while i < len(random_word):
				if random_word[i] == letter:
					guesses[i] = letter
				i = i + 1;
		else:
			max_guesses = max_guesses - 1
		
		print_word(guesses)
		
		if correct_guess(random_word, guesses):
			print 'You got it!!!!'
			break
		
		print
		if max_guesses == 0:
			print 'Sorry, no more guesses.  The word was ' + random_word	
		else:
			print 'You have ' + str(max_guesses) + ' more guesses'
	
hangman()

		