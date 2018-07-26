import csv

with open('C:\\Users\\Administrator\\Desktop\\test.csv', 'r', encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)
        print(row[0])
