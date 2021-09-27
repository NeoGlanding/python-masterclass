age = int(input('How old are you? '));

# if age > 16 and age <= 50: # penggunaan and
if 16 < age <= 50: #Simplified Chaining
    print('You are welcome to surprise me!')
else:
    print('Have a nice rest')


if age < 16 or age > 50:
    print('Have a nice rest')
else:
    print('You are welcome to surprise me!') 


today = 'Friday'
temperature = 21
raining = True

if (today == 'Friday' and temperature < 28 and not raining): #not adalah kebalikan dari value yang ada (boolean)
    print('Today is time for jogging')

