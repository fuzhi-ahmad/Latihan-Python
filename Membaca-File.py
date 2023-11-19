users = open("users.txt", "r")
print(users.read())                # Untuk cetak semua isi file
print(users.readline())            # Untuk cetak isi file perbaris, diawali dari atas .readline
array = users.readlines()           # Membuat memori array .readlines 
print(array)                       # Untuk cetak secara array semua isi file
print(array[0])                    # Untuk cetak array di baris yg di tentukan

index = 1                           # Untuk mencetak isi file sekaligus meberi index nomor                      
for user in array:
    print(f"{index} . {user}")
    index += 1
users.close()                       # menutup file tidak dibaca lagi






