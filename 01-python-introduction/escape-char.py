# Melakukan seperti enter dengan escape character \
splitString = "Hello There \nthis is escaped string \nwith \\n"
print(splitString)

# Melakukan insert "" di dalam " "
escapeCharacter = "Ihsan said \"Hello There\""
print(escapeCharacter)

# String modern dengan kemampuan dapat melakukan multi line dan escaping sendiri, dengan 3 quore
anotherLevelOfString = """Hello There "This is what ihsan said" 
I was said that
"""
print(anotherLevelOfString)

# Cara melakukan escaping untuk character \

# Cara pertama dengan dua kali \\
print("C:\\Users\\new")

# Cara kedua dengan menggunakan flag r (seolah regex)
print(r"C:\Users\new")