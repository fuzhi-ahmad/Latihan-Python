import random

#for index in range(3):
 #   print(random.randint(10, 40))

users = ['ahmad', 'agung', 'bilqis', 'filza', 'refika' ]
batas_bawah = 0
batas_atas = len(users) - 1

random_int = random.randint(batas_bawah, batas_atas)
winner = users[random_int]
print(winner)

#atau//////////
winner = random.choice(users)
print(winner)