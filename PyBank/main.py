import os
import csv

csvPath = os.path.join('Resources', 'budget_data.csv')
csvPath_out = os.path.join('Analysis', 'budget_data.txt')

with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    csv_header = next(csvReader, None)

    change = 0
    total_months = 0
    total_pnl = 0
    avg_chg = 0
    highest_ip = 0
    highest_dp = 0

    for row in csvReader:
        total_months += 1
        total_pnl += int(row[1])

        if int(row[1]) - avg_chg > highest_ip:
            highest_ip = int(row[1]) - avg_chg
            hip_month = row[0]
        elif int(row[1]) - avg_chg < highest_dp:
            highest_dp = int(row[1]) - avg_chg
            hdp_month = row[0]
            change += int(row[1])

        avg_chg = int(row[1])

with open(csvPath_out, 'w') as txtFile:

    txtFile.write('Financial Analysis\n')
    txtFile.write('----------------------------\n')
    txtFile.write('Total Months: ' + str(total_months) + '\n')
    txtFile.write('Total: $' + str(total_pnl) + '\n')
    txtFile.write("Average Change: " + str(round((change / (total_months - 1)), 2)) + '\n')
    txtFile.write('Greatest Increase in Profits: ' + hip_month + ' ($' + str(highest_ip) + ')\n')
    txtFile.write('Greatest Decrease in Profits:' + hdp_month + ' ($' + str(highest_dp) + ')\n')

with open(csvPath_out) as f:
    for line in f:
        print(line)
