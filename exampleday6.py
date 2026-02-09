import csv
with open("student.csv",mode="r")as file:
    reader=csv.ictReader(file)
    for row in reader:
        if row["status"]=="pass":
         print(row["name"])