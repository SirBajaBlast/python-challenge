# modules
import csv

# set path for file
csvpath = "Resources/budget_data.csv"

# header
print("Financial Analysis")
print("\n----------------------------")

# total months
with open(csvpath, 'r') as file:
    # skip the header
    next(file)
    
    # counter for the total number of months
    total_months = 0
    
    # iterate over each line in the file
    for line in file:
        total_months += 1

print("\nTotal Months:", total_months)

# initialize total profit/losses
total_profit_losses = 0

# total profits/losses
with open(csvpath, 'r') as file:
    
    # skip the header
    next(file)
    
    # iterate over each line in the file
    for line in file:
        # split the line by comma
        data = line.strip().split(',')
        
        # extract the profit/losses value
        profit_losses = int(data[1])
        
        # add the profit/losses to the total
        total_profit_losses += profit_losses

# print the total profit/losses as a dollar amount
print("\nTotal: ${}".format(total_profit_losses))

# average change
changes = []

# read data
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # skip the header
    header = next(csvreader)
    previous_profit_loss = None

    for row in csvreader:
        profit_loss = int(row[1])

        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)

        previous_profit_loss = profit_loss

# calculate the average of changes
average_change = sum(changes) / len(changes)

# format average change as a dollar amount
average_change_formatted = "${:.2f}".format(average_change)

# print the results
print(f"\nAverage Change: {average_change_formatted}")

# initialize variables
greatest_increase = 0
previous_profit = None
greatest_increase_date = ""

with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    
    # skip header
    next(csv_reader)
    
    for row in csv_reader:
        date = row[0]
        profit = int(row[1])
        
        if previous_profit is not None:
            profit_change = profit - previous_profit
            if profit_change > greatest_increase:
                greatest_increase = profit_change
                greatest_increase_date = date
        
        previous_profit = profit

# print the result
print(f"\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")

# initialize variables
greatest_decrease = 0
greatest_decrease_date = ""

with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    
    # skip the header row
    header = next(csv_reader)
    
    # get the first row to initialize previous profit
    first_row = next(csv_reader)

    # initialize previous profit with the profit from the first row
    previous_profit = int(first_row[1])

    for row in csv_reader:
        current_date = row[0]
        current_profit = int(row[1])

        # calculate the profit change
        profit_change = current_profit - previous_profit

        # check if the current profit change is the greatest decrease so far
        if profit_change < greatest_decrease:
            greatest_decrease = profit_change
            greatest_decrease_date = current_date

        # update previous profit for the next iteration
        previous_profit = current_profit

# print the greatest decrease in profits
print(f"\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# export the results to a text file
with open('Financial Analysis.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("\n----------------------------\n")
    f.write(f"\nTotal Months: {total_months}\n")
    f.write(f"\nTotal: ${total_profit_losses}\n")
    f.write(f"\nAverage Change: ${average_change_formatted}\n")
    f.write(f"\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    f.write(f"\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")