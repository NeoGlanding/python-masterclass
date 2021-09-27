todo_list = ['Learn Python', 'Go Swimming', 'Sleep', 'Learn Java']

while True:
    for index in range(len(todo_list)):
        print(f'{index + 1}. {todo_list[index]}')
    print('0. Quit')
    
    your_input_index = int(input('Choose one: '))
    
    if your_input_index > len(todo_list):
        print('Out of range')
        break
    elif your_input_index == 0:
        print('Thanks for playing')
        break
    
    your_input = todo_list[your_input_index - 1]

    print(f'You choose {your_input}')

