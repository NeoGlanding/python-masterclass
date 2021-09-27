import random

highest = 1000
answer = random.randint(1,highest)

print(f'Provide a answer between 0 to {highest}')
print(answer)

your_answer = int(input('Provide your answer here: '))

while your_answer != answer:
    highest = int(highest - (highest * 0.5) // 1)
    answer = random.randint(0, highest)
    print(answer)

    if (highest == 1):
        print('Game over')
        break
    

    your_answer = int(input(f'Now guess between 0 and {highest}: '))


    if (your_answer == answer):
        print('Good bro!')