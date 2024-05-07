# modules
import csv

# set path for file
csvpath = "Resources/election_data.csv"

# header
print("Election Results")
print("\n-------------------------")

# total votes
with open(csvpath, 'r') as file:
    # skip the header
    next(file)
    
    # counter for the total number of months
    total_votes = 0
    
    # iterate over each line in the file
    for line in file:
        total_votes += 1

print("\nTotal Votes:", total_votes)

print("\n-------------------------")

# calculate results
candidates = {}
winner = ""
winner_votes = 0

# read data from the csv
with open(csvpath, 'r') as file:
    csvreader = csv.reader(file)
    
    # skip the header
    next(csvreader)
    
    for row in csvreader:
        candidate = row[2]
        
        # count the votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# calculate the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = (percentage, votes)
    
    # determine the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# print the analysis
for candidate, (percentage, votes) in candidates.items():
    print(f"\n{candidate}: {percentage:.3f}% ({votes})")

print("\n-------------------------")

print(f"\nWinner: {winner}")

print("\n-------------------------")

# export the results to a text file
output_file = "Election Results.txt"

# open the output file in write mode
with open(output_file, "w") as textfile:

    # redirect the print statements to the text file
    import sys
    sys.stdout = textfile

    # header
    print("Election Results")
    print("\n-------------------------")

    # total votes
    total_votes = 0
    with open(csvpath, 'r') as file:
        next(file)
        for line in file:
            total_votes += 1
    print("\nTotal Votes:", total_votes)
    print("\n-------------------------")

    # calculate results
    candidates = {}
    winner = ""
    winner_votes = 0

    with open(csvpath, 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)

        for row in csvreader:
            candidate = row[2]

            if candidate in candidates:
                candidates[candidate] += 1
            else:
                candidates[candidate] = 1

        for candidate, votes in candidates.items():
            percentage = (votes / total_votes) * 100
            candidates[candidate] = (percentage, votes)

            if votes > winner_votes:
                winner = candidate
                winner_votes = votes

        for candidate, (percentage, votes) in candidates.items():
            print(f"\n{candidate}: {percentage:.3f}% ({votes})")

        print("\n-------------------------")
        print(f"\nWinner: {winner}")
        print("\n-------------------------")

    # reset the standard output to the console
    sys.stdout = sys.__stdout__