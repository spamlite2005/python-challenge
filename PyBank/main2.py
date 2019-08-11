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
        profit_loss = profit_loss + int(row[1])
        print(row[0], row[1])

    print(str(months))
    print(str(profit_loss))
    avg_profit_loss = round(profit_loss / months, 2)
    print(str(avg_profit_loss))

    max_profit_loss = max(int(row[1]))
    print(str(max_profit_loss))

    min_profit_loss = min(int(row[1]))
    print(str(min_profit_loss))