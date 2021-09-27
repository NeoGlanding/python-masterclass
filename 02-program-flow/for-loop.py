parrot = 'Norwegian Blue'

for character in parrot: #mengulang parrot, dan setiap perulangan di simpan dalam character
    print(character)

numerics = '323:321;321;221;3231.321,434.233'
separators = ''

for separator in numerics:
    if not separator.isnumeric():
        separators = separators + separator

print(separators)