import random

highest = 10
answer = random.randint(1, highest)

your_answer = int(input('Provide your answer here: '))

print('Challenge guess a number')
while your_answer != answer:
    if (your_answer > answer):
        print('Guess it lower')
    else:
        print('Guess it higher')
    your_answer = int(input('Guess it: '))