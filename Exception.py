try:
    level = input("Level kamu :")
    level = int(level)
    print(level)
except ValueError:
   print("Yang kamu masukan bukan angka loh")
# atau ///////////////////////////////
except:
    print("terjadi kesalahan")