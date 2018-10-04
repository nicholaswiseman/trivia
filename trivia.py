import random
import os

def get_qs():
	while 1:
		q_dict = {}
		category = input('Please choose a category:\n(r=random h=history m=music g=geography)\n\n')
		try:
			file = open(f'{category}.txt','r')
		except:
			print('Invalid category!\n')
		else:
			lines = file.readlines()
			for line in lines:
				[q_str, a_str] = line.split(':')
				q_dict[q_str] = a_str.rstrip()
			file.close()
			return q_dict

def ask_a_q():
	question = questions[random.randint(0,len(questions)-1)]
	#remove the question from list of questions as to not ask again
	questions.remove(question)
	answer = input(f'{question}\n').lower()
	if qs_and_as[question].lower() == answer:
		return True
	else:
		print(f'Sorry! The correct answer was: {qs_and_as[question]}')
		return False

	
if __name__ == '__main__':
	os.system('cls')
	print('Hello! Welcome to...')
	print(' _______  ______    ___   __   __  ___   _______') 
	print('|       ||    _ |  |   | |  | |  ||   | |   _   |')
	print('|_     _||   | ||  |   | |  |_|  ||   | |  |_|  |')
	print('  |   |  |   |_||_ |   | |       ||   | |       |')
	print('  |   |  |    __  ||   | |       ||   | |       |')
	print('  |   |  |   |  | ||   |  |     | |   | |   _   |')
	print('  |___|  |___|  |_||___|   |___|  |___| |__| |__|')
	print('\n')
	while 1:
		qs_and_as = get_qs()
		questions = list(qs_and_as.keys())
		num_qs = 5
		score = 0
		
		for num in range(num_qs):
			print(f'\nQuestion #{num+1}:')
			correct = ask_a_q()
			if correct:
				score+=1
				print("Correct!")
			
		print(f'\nYour score is {score}/{num_qs}!')
		if input("Play again? (yes/no)").lower() != 'yes':
			break
	
	
	