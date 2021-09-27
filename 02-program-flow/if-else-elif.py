# If menandakan jika ada kondisi tertentu maka akan.

name = input("What is your name: ")
age = int(input("What is your age: "))

# if age > 18: # Jika berusia diatas 18 tahun
#     print('You are legal to drive a car')
# else: # Kalau berusia tidak diatas 18 tahun
#     print(f'Please comeback in {18 - age} years to get a license')

if age < 18:
    print(f"Anda tidak boleh mengendarai mobil, kembali dalam {19 - age} tahun");
elif age == 200: # Kondisi selain if dan else
    print(f"Special conditions")
else:
    print("Anda di izinkan mengendarai mobil")


answer = 3
guess = int(input("Guess a number between 1 to 10: "))


# if bersarang
if guess > answer:
    print("Guess it lower")
    guess = int(input())
    if guess == answer:
        print("You guessed correctly")
    else:
        print("You wrong")
elif guess < answer:
    print("Guess it higher")
    guess = int(input())
    if guess == answer:
        print("You guessed correctly")
    else:
        print("You wrong")
else:
    print("You correct")