import csv

users = open("users.csv", "r")

users_csv = csv.reader(users, delimiter=",")

for row in users_csv:
    print(f"Nama : {row[0]}. Panggilan : {row[1]}. Status : {row[-1]}")

users.close()