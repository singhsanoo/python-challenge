from audioop import avg
import csv
import os
from sqlite3 import Date
from statistics import mean


file_path = os.path.join(".", "Resources", "budget_data.csv")
row_count = 0
total = 0
temp = 0
change_dict = {"Date":[],"P/L":[]}

with open (file_path, 'r') as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    #Storing the header
    csv_header = next(file)

    for row in file:
        #To count total number of months
        row_count += 1

        #get net total amount of "Profit/Losses"
        total += int(row[1])

        #Calulating changes in "Profit/Losses" over the entire period
        change = int(row[1]) - temp
        temp = int(row[1])

        #Creating a dictionary with change value and Date
        change_dict["Date"].append(row[0])
        change_dict["P/L"].append(change)


#removing 1st values from the dictonary       
change_dict["Date"].pop(0)
change_dict["P/L"].pop(0)

#get the index value of greatest increase in profit and greates decrease in profit
g_inc_pro_ind = change_dict["P/L"].index(max(change_dict['P/L']))
g_dec_pro_ind = change_dict["P/L"].index(min(change_dict['P/L']))

  
result = f"""
Financial Analysis
{'-'*30}
Total Months: {row_count}
Total: ${total}
Average Change: ${round(mean(change_dict['P/L']),2)}
Greatest Increase in Profits: {change_dict["Date"][g_inc_pro_ind]} (${max(change_dict['P/L'])})
Greatest Decrease in Profits: {change_dict["Date"][g_dec_pro_ind]} (${min(change_dict['P/L'])})
"""

print(result)

#Write Output to the text file
output_path = os.path.join(".", "analysis", "result.txt")
with open (output_path, 'w') as textfile:
    textfile.write(result)