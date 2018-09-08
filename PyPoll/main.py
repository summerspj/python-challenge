#PyPoll Main.py - reads a file of election data, summarizes votes and candidates and identifies a winner 
# Output is presented to terminal and an output file.
# Input data contains "Voter ID", "County", and "Candidate" and includes header.  File contains 3,521,003 rows (including header)

import os
import csv
# importing reduce()
from statistics import mean

electionIn_csv = os.path.join("", "", "election_data.csv")

#initialization
totalVotes = 0
candidate = []
winner = {}
KhanTotal = 0
CorreyTotal = 0
LiTotal = 0
OTooleyTotal = 0
KhanPercent = 0.0
CorreyPercent = 0.0
LiPercent = 0.0
OTooleyPercent = 0.0
    
# open file and read

with open(electionIn_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # for each row, add to total and add candidate voted for to list
    for row in csvreader:
        totalVotes += 1
        # Add title
        candidate.append(row[2])

# count the total votes in candidate list
KhanTotal = candidate.count("Khan")
CorreyTotal = candidate.count("Correy")
LiTotal = candidate.count("Li")
OTooleyTotal = candidate.count("O'Tooley")

# get percent of votes for each candidate
KhanPercent = (KhanTotal/totalVotes) * 100
CorreyPercent = (CorreyTotal/totalVotes) * 100
LiPercent = (LiTotal/totalVotes) * 100
OTooleyPercent = (OTooleyTotal/totalVotes) * 100 

# add percent for each candidate to winner list
winner["Khan"] = KhanPercent
winner["Correy"] = CorreyPercent
winner["Li"] = LiPercent
winner["O'Tooley"] = OTooleyPercent


# get largest percent winner
maximum = max(winner, key=winner.get)  # Just use 'min' instead of 'max' for minimum.



# print report
print(f'Election Results')
print(f'-------------------------------')
print(f'Total Votes:  {totalVotes}')
print(f'-------------------------------')
print(f'Khan:  {round(KhanPercent): .3f} ({KhanTotal})')
print(f'Correy:  {round(CorreyPercent): .3f} ({CorreyTotal})')
print(f'Li:  {round(LiPercent): .3f} ({LiTotal})')
print(f"O'Tooley:  {round(OTooleyPercent): .3f} ({OTooleyTotal})")
print(f'-------------------------------')
print(f'Winner: {maximum}')
print(f'-------------------------------')

# put report to output
output_file = os.path.join("electionRpt.txt")

with open("electionRpt.txt", "w") as text_file:
    text_file.write(f'Election Results\n')
    text_file.write(f'-------------------------------\n')
    text_file.write(f'Total Votes:  {totalVotes}\n')
    text_file.write(f'-------------------------------\n')
    text_file.write(f'Khan:  {round(KhanPercent, 3)} ({KhanTotal})\n')
    text_file.write(f'Correy:  {round(CorreyPercent, 3)} ({CorreyTotal})\n')
    text_file.write(f'Li:  {round(LiPercent, 3)} ({LiTotal})\n')
    text_file.write(f"O'Tooley:  {round(OTooleyPercent, 3)} ({OTooleyTotal})\n")
    text_file.write(f'-------------------------------\n')
    text_file.write(f'Winner: \n')
    text_file.write(f'-------------------------------\n')










 