import csv
import os

csv_path = os.path.join("Resources", "budget_data.csv")

months = 0
profit_loss = 0

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        months = months + 1
        profit_loss = int(row[1])
    
    print(str(months))
    print(str(profit_loss))

