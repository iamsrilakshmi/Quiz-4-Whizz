questions=('How many continents in this world ?',
'How many planets in the Universe ?',
'How many hours in a day ?',
'How many days in a year ?',
'How many days in a week',
'What is the smallest prime number ?',
'What is the LCM of 2 &3 ?',
'What is the square of 11 ?',
'What is 10 to the power of 4 ?',
'How many zeros in 1 billion ?'
)
answers=('7','9','24','365','7','2','6','121','10000','9')

score=0


def quiz():
	print('Welcome TO QUIZ 4 WHIZZ created by SRI LAKSHMI')
	print('Each correct answer would be awarded a score of 1')
	print(' ALL THE BEST...!!!')
	global score
	index=0
	for q in questions:
		print(q)
		ans = input('Enter your answer : ')
		if ans == answers[index]:
			score += 1
		index += 1
	return score

def final():
	final_score =quiz()
	print('\n\nCongratulations...!!!\nYour Total Score is : ', final_score)
	if final_score ==10:
		print('\nWowww...!!! You are a genius & a real Whizz')
	else:
		correct_ans='''
CORRECT ANSWERS FOR THE QUIZ ARE:

How many continents in this world ? : 7
How many planets in the Universe ? : 9
How many hours in a day ? : 24
How many days in a year ? : 365
How many days in a week : 7
What is the smallest prime number ? : 2
What is the LCM of 2 & 3 ? : 6
What is the square of 11 ? : 121
What is 10 to the power of 4 ? : 10000
How many zeros in 1 billion ? : 9
		'''
		print(correct_ans)

	print('Thank you for your participation in QUIZ 4 WHIZZ...!!!\n\n ')

if __name__=='__main__':
	final()
