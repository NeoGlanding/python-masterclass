# Slicing adalah proses mengambil string bedasarkan start and stop

nama = "Muhammad Ihsan Abdurrahman"

# Mengambil nama dari index 0, dan berakhir di 2 (3 tidak termasuk)
print(nama[0:3]) #Muh

# Mengambil nama dari index ke 5, sampai akhir
print(nama[3:]) # ammad Ihsan Abdurrahman

# Mengambil dari index 0 sampai index 10 (11 tidak termasuk)
print(nama[:11])

# Mengambil dari index ke 4 dari belakang sampai ke 3 dari belakang (2 tidak termasuk)
print(nama[-4:-2])

# Mengambil dari awal sampai akhir, tapi diambil setiap dua langkah
print(nama[0::2]) #Mhma ha burha