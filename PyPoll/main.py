# Objective 1: Import modules os and csv. Importing numpy in order to use the unique function
import os
import csv

# Objective 2: Set the path for the CSV file 
election_csv = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')

# Objective 3: Create the lists to store data. Initialize
candidate_list = []
unique_candidate_list = []
vote_count_list = []
vote_percent_list = []

# Objective 4: Initialize the variables
vote_count = 0

# Objective 5: Open the CSV using the set path
with open(election_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # 5.01 Skip the header row
    csv_header = next(csv_reader)

    # Objective 6: Begin looping through the csv
    for row in csv_reader:
        
        # 6.01 Count the total number of votes
        vote_count = vote_count + 1
        
        # 6.02 Add the candidate names to the candidate list
        candidate_list.append(row[2])
        
        # 6.03 Create a set from the candidate list to get the unique candidate names
    for x in set(candidate_list):

        # 6.04 Add the unique names to a unique candidate list
        unique_candidate_list.append(x)
        
        # 6.05 y is the total number of votes per candidate
        y = candidate_list.count(x)

        # 6.06 Add the number of votes to the vote count list
        vote_count_list.append(y)
       
        # 6.07 z is the percent of total votes per candidate
        z = (y/vote_count)*100

        # 6.08 Add the percentages to the vote percent list
        vote_percent_list.append(z)

    # Objective 7: Find the highest value in the vote count list    
    winning_vote_count = max(vote_count_list)

    #7.01 Find the corresponding unique name for the max vote count
    winner = unique_candidate_list[vote_count_list.index(winning_vote_count)]


# Objective 8: Print to terminal
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes: " + str(vote_count))    
print("-------------------------")
# 8.01 Print for every name in the unique candidate list
for i in range(len(unique_candidate_list)):
            print(unique_candidate_list[i] + ": " + str(vote_percent_list[i]) +"% (" + str(vote_count_list[i])+ ")")
print("-------------------------")
print("The winner is: " + winner + "!")
print("-------------------------")

# Objective 9: Open file to begin writing text
with open("/Users/candacestingley/Documents/GitHub/Python_Challenge/PyPoll/Analysis/election_analysis.txt", "w") as text:

    # 9.01 Write each row
    text.write("------------------------------------------ \n\n")
    text.write("Election Results \n\n")
    text.write("------------------------------------------  \n\n")
    text.write("Total Votes: " + str(vote_count) + "\n\n")
    text.write("------------------------------------------  \n\n")
    # 9.02 Write for every name in the unique candidate list
    for i in range(len(unique_candidate_list)):
            text.write(unique_candidate_list[i] + ": " + str(vote_percent_list[i]) +"% (" + str(vote_count_list[i])+ ")" + "\n\n")
    text.write("------------------------------------------  \n\n")
    text.write("The winner is: " + winner + "!" + "\n\n")
    text.write("------------------------------------------  \n\n")
