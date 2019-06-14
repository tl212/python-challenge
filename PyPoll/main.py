import os
import csv

csvPath = os.path.join('Data', 'election_data.csv')
csvPath_out = os.path.join('Analysis', 'election_data.txt')

with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    csv_header = next(csvReader, None)

    total_votes = 0
    candidates = []
    votes = []

    for row in csvReader:
        total_votes += 1
        if row[2] in candidates:
            votes[candidates.index(row[2])] += 1
        else:
            candidates.append(row[2])
            votes.append(1)

with open(csvPath_out, 'w') as txtFile:
    txtFile.write('Election Results' + '\n')
    txtFile.write('-------------------------' + '\n')
    txtFile.write('Total Votes: ' + str(total_votes) + '\n')
    txtFile.write('-------------------------' + '\n')

    for y in range(len(candidates)):
        txtFile.write(
            candidates[y] + ': ' + str(format(votes[y] / total_votes * 100, '.3f')) + '% (' + str(votes[y]) + ')\n')
    txtFile.write('-------------------------' + '\n')
    txtFile.write('Winner: ' + candidates[votes.index(max(votes))] + '\n')
    txtFile.write('-------------------------')

with open(csvPath_out) as f:
    for line in f:
        print(line)






