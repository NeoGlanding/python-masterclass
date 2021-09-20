# > untuk rata kanan
# < untuk rata kiri
# :8 untuk spasi

for i in range(1,11):
    print("No {0:8}, cubed is {1:>9}, squared is {2}".format(i, i ** 2, i **3))

# f-strings, sama seperti backtick pada js, untuk melakukan formatting
nama = "Ihsan"
print(f"Hallo nama saya {nama}")