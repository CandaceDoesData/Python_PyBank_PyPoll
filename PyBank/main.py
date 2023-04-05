# Objective 1: Import modules os and csv
import os
import csv

# Objective 2: Set the path for the CSV file in PyBankcsv
budget_csv = os.path.join('..','PyBank', 'Resources', 'budget_data.csv')

# Objective 3: Create the lists to store data. 
dates_list = []
profits_list = []
changes_list = []

# Objective 4: Initialize the variables 
month_count = 0
total_profit = 0

last_month_profit = 0
total_change_profit = 0

# Objective 5: Open the CSV using the set path 
with open(budget_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # 5.01: Skip the file header
    next(csv_reader, None)

    # Objective 6: Conducting the ask/ begin looping through csv
    for row in csv_reader:

        # 6.01 Count the number months in this dataset
        month_count = month_count + 1

        # 6.02 Add the date info to the date list. 
        # Will need it when collecting the greatest increase and decrease in profits
        dates_list.append(row[0])
        
        # 6.03 Calculate the total profit
        total_profit = total_profit + int(row[1])

        # 6.04 Calculate the change in profits from month to month.
        this_month_profit = int(row[1])
        month_change_profit = this_month__profit - last_month_profit

        # 6.05 Store these monthly changes in a list
        changes_list.append(month_change_profit)

        # 6.06 Set the first value of the list to 0
        changes_list[0] = 0

        # 6.07 Reset the change calculation loop
        last_month_profit = int(row[1])

        # 6.08 Calculate the total of the changes
        total_change_profit = sum(changes_list)

        # 6.09 Calculate the average change in profits
        average_change_profit = total_change_profit / 85

        # 6.10 Find the max change in profits
        greatest_increase = max(changes_list)

        # 6.11 Find the min change in profits
        greatest_decrease = min(changes_list)

        # 6.12 Find the corresponding date for the max
        increase_date = dates_list[changes_list.index(greatest_increase)]

        # 6.13 Find the corresponding date for the min
        decrease_date = dates_list[changes_list.index(greatest_decrease)]

# Objective 7: Print results to Terminal
print("Financial Analysis")
print("-------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_profit))
print("Average Change: $" + str(average_change_profit))
print("Greatest Increase in Profits: " + str(increase_date) + (" $") + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(decrease_date) + (" $") + str(greatest_decrease))


# Objective 8: Open file to begin writing text
with open("/Users/candacestingley/Documents/GitHub/Python_Challenge/PyBank/Analysis/financial_analysis.txt", "w") as text:

    # 8.01 Write each row
    text.write("------------------------------------ \n\n")
    text.write("Financial Analysis \n\n")
    text.write("------------------------------------ \n\n")
    text.write("Total Months: " + str(month_count) + "\n\n")
    text.write("Total: $" + str(total_profit) + "\n\n")
    text.write("Average Change: $" + str(average_change_profit) + "\n\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + (" $") + str(greatest_increase) + "\n\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + (" $") + str(greatest_decrease) + "\n\n")

