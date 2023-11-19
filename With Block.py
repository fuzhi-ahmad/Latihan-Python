import csv

with open("users.csv", "r") as users:
    users_csv = csv.reader(users, delimiter=",")
    for row in users_csv:
        print(f"Nama : {row[0]}. Panggilan : {row[1]}. Status : {row[-1]}")
