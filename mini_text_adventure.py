import random

choices = ('north', 'south', 'east', 'west')
score = 0

while True:
	print('You are in a forest, do you go North, South, East or West?')
	direction = input('> ').lower()
	if direction not in choices:
		print('Invalid choice')
		continue
	bad_choices = random.sample(choices, 2)
	if direction in bad_choices:
		print('You have been eaten by a bear')
		break
	else:
		print('Keep going...')
		score += 1
		
print('Game over! You scored', score)
