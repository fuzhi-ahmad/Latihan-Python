
print("================================")
print("FORM REGISTRATION")
name = input("Nama : ")
nim = int(input("Nim : "))
total_price =int(input("Total Price : "))
shipping_cost = int(input("Shipping Cost : "))
discount = 0.1

print("===============================")
def Hello_User(name, nim):
    print(f"Hello {name}-{nim}")
    print("Selamat Belajar Python")

print("Start")
Hello_User(name, nim)
print("===============================")
calculate_total_cost = (total_price - (total_price * discount )) + (shipping_cost)
calculate_total_cost = int(calculate_total_cost)
print( "Jumlah yang harus di bayar Rp.",calculate_total_cost)
print("Finish")

