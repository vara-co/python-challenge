# Declare / Import the dependencies
import os
import csv

# Specify the path to the CSV file election_data.csv
electionData_csv = os.path.join("Resources", "election_data.csv")

# Variables to store total votes
totalVotes = 0

#Create a dictionary to store the number of votes each candidate receives
candidates_votes = {}

# Open and read the data of the CSV file.
with open(electionData_csv) as data:

    # Initiate the reader
    reader = csv.reader(data, delimiter=",")

    # Skip the header row when looping through the data
    header = next(reader)

    #--------------------------------------------------
    #-----------         L  O  O  P         -----------
    #--------------------------------------------------

    # Start your loop over the rows to make calculations
    for row in reader:

        # Get the candidate name from the current row.
        # Names are in index 2
        candidate_name = str(row[2])

        # -----------------------------------------------
        # ----------        Conditionals        ---------
        # -----------------------------------------------

        # Check if candidate name is in the dictionary
        #If not, adds candidates with initial count of cero
        if candidate_name not in candidates_votes:
            candidates_votes[candidate_name] = 0

        #Add votes to each candidate in increments of 1 using += operator
        candidates_votes[candidate_name] += 1

        #Calculate the total votes in increments of 1 using += operator
        totalVotes += 1


# Print the outcomes in the console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")

#Loop to find out how many votes & % per candidate and print to console
#This loop has to be here rather than before the 'Print outcomes' section
#otherwise, it won't print all of the candidates in the format required
for candidate_name, totalVotesCandidate in candidates_votes.items():

    #Calculate the percentage of each candidate's votes
    percent = (totalVotesCandidate / totalVotes) * 100
    #Format the percentage to round to 3 decimals
    percentFormat = float(round(percent,3))

    #Variable to save the results to print out
    result = f"{candidate_name}: {percentFormat}% ({totalVotesCandidate})"
    print(result)

#Finding out who won and printing it out to console
#Store in 'winner' variable. Use the max function for the maximum value
#Search these values through the candidates_votes dictionary
#Use the get method to retrieve the value associated with the key
winner = max(candidates_votes, key=candidates_votes.get)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#--------------------------------------------------------------------------
#------       Printing the resulting analysis into a text file       ------
#--------------------------------------------------------------------------

#Specify the output file path
output_path = os.path.join("analysis", "PyPoll_analysis.txt")

# Open the file in write mode and redirect the print statements to the file
with open(output_path, "w") as textfile:

    #Inicialize the txt.writer function to write the variable we created
    csvwriter = csv.writer(textfile)

    #Writing the 'Election Results' and the 'Total Votes' to the txt file
    #csvwriter.writerow([""])  Write within parenthesis the outcomes to be written
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {totalVotes}"])
    csvwriter.writerow(["-------------------------"])

    #Writing the candidates with their number of votes and the percentage of such votes
    #This for loop has to be repeated here. Otherwise it is not printing
    #all of the candidates and their outcome in the format required in the txt file
    for candidate_name, totalVotesCandidate in candidates_votes.items():
        percent = (totalVotesCandidate / totalVotes) * 100
        percentFormat = float(round(percent, 3))
        result = f"{candidate_name}: {percentFormat}% ({totalVotesCandidate})"

        # Writing the result to the text file
        csvwriter.writerow([f"{result}"])

    #Writing the winner with it's format to the txt file
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])