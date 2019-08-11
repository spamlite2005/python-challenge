import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r', newline='', ) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header is: {csv_header}")
    votes = 0
    for row in csvreader:
        votes = votes + 1
    print(f"There were {votes} total votes.")

    VoterID = list(csv.reader(csvreader[0]))
    County = list(csv.reader(csvreader[1]))
    Candidate = list(csv.reader(csvreader[2]))

    Candidate.head()


