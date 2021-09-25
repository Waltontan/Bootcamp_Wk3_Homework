import csv
from os import error, name

# Set csv file path
filepath = "Resources/election_data.csv"

# Open CSV file and set delimiter
with open(filepath, "r") as file:
    csvreader = csv.reader(file,delimiter=",")

    # Skip and store column header in 'header'
    header = next(csvreader)

    # Creat list for voted names
    Candidate = []
    for rows in csvreader:
        Candidate.append(rows[2])

    # Create list of unique candidates names
    Name = []

    # Create a list with unique values to find out how many candidates there are
    for rows in Candidate:
        try:
            Name.index(rows)    # Try if current voted name is already in the 'Name' list
        except ValueError:
            Name.append(rows)   # If the voted name is not in the list it'll return a ValueError and the voted name will be added to the 'Name' list

    # Create a list to store the number of vote each candidate gets
    Counter = 0
    Vote = 0
    SumVote = []
    
    while Counter < len(Name): # Use a 'Counter' to loop as long as it is less than the number of candidates
        for rows in Candidate:  # Loop through all votes
            if rows == Name[Counter]:   # Check if Name on the Vote is the same as the name that is totalling up now
                Vote = Vote + 1 # Increase count if voted name is equals to the current Name
        SumVote.append(Vote)
        Vote = 0
        Counter = Counter+1

    # Create list of percentage of each Candidate
    percent = []

    for rows in SumVote: # Loop through 'SumVote' list
        percent.append(round((rows/len(Candidate))*100,2)) # Find percentage by dividing votes for each candidate will all votes (len/count of the 'Candidate' list)

    # Find Winner
    HighestPercent = 0
    for rows in percent: # Loop through 'percent' list
        if rows > HighestPercent: # Only overwrite the 'HighestPercent' is the value is higher than the current 'HighestPercent'
            HighestPercent = rows
    
    Winner  = Name[percent.index(HighestPercent)] # Find index of the Highest percentage in the 'percent' List and correspond the index with the 'Name' list to find the winner

    print("-------------------------")
    print("Election Results") # Print Title
    print("-------------------------")
    print(f"Total Votes: {len(Candidate)}") # Print total number of votes by calculating number of variables in candidate vote list
    print("-------------------------")
    
    # Loop to Print Candidate Name with their percentage vote and number of votes
    Counter = 0
    while Counter < len(Name):
        print(f"{Name[Counter]}: {percent[Counter]}% ({SumVote[Counter]})")
        Counter = Counter + 1
    
    print("-------------------------")
    print(f"Winner: {Winner}") # Print Winner
    print("-------------------------")




# Specifying output location and name of new text file
output_path = "Resources/election_results.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as file:

    file.write("-------------------------")
    file.write('\n')
    file.write("Election Results") # Print Title
    file.write('\n')
    file.write("-------------------------")
    file.write('\n')
    file.write(f"Total Votes: {len(Candidate)}")
    file.write('\n')
    # Loop to Print Candidate Name with their percentage vote and number of votes
    Counter = 0
    while Counter < len(Name):
        file.write(f"{Name[Counter]}: {percent[Counter]}% ({SumVote[Counter]})")
        file.write('\n')
        Counter = Counter + 1
    file.write("-------------------------")
    file.write('\n')
    file.write(f"Winner: {Winner}") # Print Winner
    file.write('\n')
    file.write("-------------------------")
    file.write('\n')