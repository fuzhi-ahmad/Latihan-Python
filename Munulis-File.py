users = open("users.txt", "a")   # Mode r (readable), w (writeable + hapus isi file lama), r+ (readable,writeable) a (menambah file yg sudah ada)
print(users.writable())          # Check enable mode nya
print(users.readable())          # Jika nama file belum ada kitika pakai mode (w) akan di buatkan file baru

users.write("\n Imam Rusdiono - imam - Adik")

users.close()