numbers = [1,2,4,7,34,533]

for number in numbers:
    if number % 5 == 0:
        print('This is unnacceptable numbers')
        break
else: #jika di for loop tidak ada kondisi yang terpenuhi
    print('Good, all numbers are accepted')