#PyBank Main.py - reads a file of months and profit/loss, 
# Calculates some differences in profit/loss, write out a report on terminal and to output file

import os
import csv
# importing reduce()
from statistics import mean

# initialize
budgetIn_csv = os.path.join("", "", "budget_data.csv")

totalMonths = 0
totalNetProfits = 0
triggerSave = 1
changeInProfitLoss = []
savedProfitChg = 0
savedLossChg = 0
savedLossMo = ""
savedProfitMo = ""
firstRow = 1

# function to defin average
def Mean(changeInProfitLoss = []):
#    return float(sum(changeInProfitLoss)) / max(len(changeInProfitLoss), 1)
    return mean(changeInProfitLoss)
    
# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(budgetIn_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#psuedocode for logic with each row
# For each row
    # If first time through - set up initialization
        # If PL is >= 0 
            # save profit month
            # save profit PL
        # else
            # save loss month
            # save loss PL
        #Previous PL = row

    # Chg = current PL - Previous PL
    # If chg > prev profit change
        # Save current month and change as greatest profit
    # If chg < prev profit loss
        # Save current month and change as greatest loss 
    # Save chg as monthly change

    # Save current row - month and profit/loss
    for row in csvreader:
        if triggerSave == 1:
            if int(row[1]) >= 0:
                savedProfitMo = str(row[0])
                savedProfitChg = 0
            else: 
                savedLossMo = str(row[0])
                savedLossChg = 0
            triggerSave = 0
            prevPL = int(row[1])
#            prevPL = 0
    

        totalMonths += 1
        totalNetProfits = totalNetProfits + int(row[1])
 
        chgInPL = int(row[1]) - prevPL
        if chgInPL > savedProfitChg:
            savedProfitMo = str(row[0])
            savedProfitChg = chgInPL
        elif (chgInPL < savedLossChg):
            savedLossMo = str(row[0])
            savedLossChg= chgInPL

        if firstRow == 1:
            firstRow = 0
        else:
            changeInProfitLoss.append(chgInPL)

        prevPL = int(row[1])

# Call average function using profitloss list
average = Mean(changeInProfitLoss)

#Terminal print

print(f'Financial Analysis')
print(f'Total Months:  {totalMonths}')
print(f'Total Net Amount:  ${totalNetProfits}')
print(f'Average change in profit/loss over {totalMonths} months:  ${average: .2f}')
print(f'The greatest increase in profits: {savedProfitMo} (${savedProfitChg})')
print(f'The greatest decrease in profits: {savedLossMo} (${savedLossChg})')

# write output to file

output_file = os.path.join("budgetOut.txt")

with open("budgetOut.txt", "w") as text_file:
    text_file.write(f'Financial Analysis\n')
    text_file.write(f'Total Months:  {totalMonths}\n')
    text_file.write(f'Total Net Amount:  {totalNetProfits}\n')
    text_file.write(f'Average change in profit/loss over {totalMonths} months:  {round(average, 2)}\n')
    text_file.write(f'The greatest increase in profits: {savedProfitMo} ({savedProfitChg})\n')
    text_file.write(f'The greatest decrease in profits: {savedLossMo} ({savedLossChg})\n')
 