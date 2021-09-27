parrot = 'Norwegian Blue'

text = input('Enter your text here: ')

if text in parrot.casefold(): #casefold untuk melakukan lowercasing (sampai ke unicode)
    print(f'{text} is in {parrot}')
else:
    print('You should check')


activity = 'Cinema, Footballing'

text2 = input('Enter your activity: ')

if text2 not in activity.casefold():
    print("Gak ada")
else:
    print('Ada')