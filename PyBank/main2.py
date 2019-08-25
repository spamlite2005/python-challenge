# Import dependencies
import csv
import os

# Create Path and open file and declare header
csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# Initialize variables for months, profit_loss, Maximum, Minimum, Average. And create new Dictionary called 'mydict'
    months = 0
    profit_loss = 0
    max_profit_loss = 0
    min_profit_loss = 0
    avg_profit_loss = 0 
    mydict = {}

# Loop through csvfile to create the dictionary
    for row in csvreader:
        k = row[0]
        v = int(row[1])
        mydict[k] = int(v)
        months = months + 1
        profit_loss = profit_loss + int(v)
        monthly_change = [profit_loss + int(v)]
        bigprofit = profit_loss + int(v)
        bigloss = profit_loss + int(v)
#        min_profit_loss = min_profit_loss + int(v)
        if bigprofit < int(v):
            bigprofit = int(v)
        if bigloss > int(v):
            bigloss = int(v)
#    print(mydict)
    print("")
    print(f"Financial Analysis")
    print("-----------------------------    -------")
    print(f"Total months: {months}")
    print(f"Net profit/loss is: ${profit_loss}")
    avg_profit_loss = round((profit_loss) / months,2)
    print(f"Average Change: ${avg_profit_loss}")
    print(f"Greatest Increase in Profit: ${round(bigprofit,2)}")
    print(f"Greatest Decrease in Profit: -${round(bigloss,2)}")