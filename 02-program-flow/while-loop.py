# start_condition = 0

# while start_condition < 10:
#     print('Hello World')
#     start_condition += 1

exits = ['east', 'west', 'north', 'south']

your_position = ''
while your_position not in exits:
    your_position = input('Where are you now? ')
    wanna_quit = input('Do you wanna stay in circle of satan? ')
    if wanna_quit.casefold() == 'yes':
        print('You are in satan circle')
        break

print('I\'m Glad you are out from the circle of satan')