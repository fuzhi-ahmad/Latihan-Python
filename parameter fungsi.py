# Fungsi menggunakan def/ definisi untuk membungkus intruksi-intruksi.
# Parameter Fungsi
print("================================")
print("FORM REGISTRATION")
name1 = input("Nama : ")
nim1 = int(input("Nim : "))
name2 = input("Nama : ")
nim2 = int(input("Nim : "))
print("===============================")
def Hello_User(name1, nim1):
    print(f"Hello {name1}-{nim1}")
    print("Selamat Belajar Python")

print("Start")
Hello_User(name1, nim1)
print("===============================")
Hello_User(name2, nim2)
print("Finish")

