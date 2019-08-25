import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r', newline='', ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header is: {csv_header}")
    
    khan = 0
    correy = 0
    li = 0
    otooley = 0

    votes = 0
    for row in csvreader:
        votes = votes + 1
        if row[2] == 'Khan':
            khan = khan + 1
        elif row[2] == 'Correy':
            correy = correy + 1
        elif row[2] == 'Li':
            li = li +1
        elif row[2] == "O'Tooley":
            otooley = otooley + 1
    khan_pc = round(100*khan/votes, 4)
    correy_pc = round(100*correy/votes, 4)
    li_pc = round(100*li/votes, 4)
    otooley_pc = round(100*otooley/votes, 4)


    names = {"Khan": khan, "Correy": correy, "Li": li, "O'Tooley" : otooley}
    winner = max(names)
    winnername = winner

    print(f"Election Results")
    print(f"--------------------------")        
    print(f"Total Votes: {votes}")
    print(f"--------------------------") 
    print(f"Khan: {khan_pc}% ({khan})")
    print(f"Correy: {correy_pc}% ({correy})")
    print(f"Li: {li_pc}% ({li})")
    print(f"O'Tooley: {otooley_pc}% ({otooley})")
    print(f"--------------------------") 
    print(f"Winner {winnername}")
    print(f"--------------------------") 



