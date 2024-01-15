# python-challenge
DU - DA Module 3
--------------------------------
--------------------------------
PYTHON CHALLENGE
--------------------------------
--------------------------------
by Laura Vara
--------------------------------
Note: It is important that if you are going to use this code, the csv files
are placed in a directory called Resources, in the same directory as your
main python file. Otherwise the code with the path were you intend to read 
your csv file, needs to be updated to where the new path is located for the
csv file. This applies for both PyBank and PyPoll. Ideally they will be set
in the same way they are found in this repository.

This repository consists of two challenges:
1. PyBank
2. PyPoll

---------------------------------
INDEX
---------------------------------
1. Content of the repository
2. Instructions for each of the Python challenges
3. References

---------------------------------
Content of the repository
---------------------------------
1. Directory with the PyBank python challenge:
• main.py file with the code
• Resources directory with budget_data.csv file
• analysis directory with PyBank_analysis.txt file

2. Directory with the PyPoll python challenge:
• main.py file with the code
• Resources directory with election_data.csv file
• analysis directory with PyPoll_analysis.txt file

----------------------------------
Instructions for PyBank
----------------------------------
PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:
• The total number of months included in the dataset
• The net total amount of "Profit/Losses" over the entire period
• The changes in "Profit/Losses" over the entire period, and then the average of those changes
• The greatest increase in profits (date and amount) over the entire period
• The greatest decrease in profits (date and amount) over the entire period
• In addition, your final script should both print the analysis to the terminal and export a text file with the results.

----------------------------------
Instructions for PyPoll
----------------------------------
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
• The total number of votes cast
• A complete list of candidates who received votes
• The percentage of votes each candidate won
• The total number of votes each candidate won
• The winner of the election based on popular vote
• In addition, your final script should both print the analysis to the terminal and export a text file with the results.

------------------------------------
References for PyBank and PyPoll
------------------------------------
Most of what's in these two challenges, was covered in class.
The few things that either weren't or I had to reference to, are described
with it's source right below.

=PyBank=
Obtaining the Min and Max values, were there are negative values in the amounts, 
was referenced from:
https://www.geeksforgeeks.org/python-infinity/

Adding one to the count with the +=, was referenced from:
https://www.w3schools.com/python/python_operators.asp

=PyPoll=
Using 'not in' for the conditionals, was referenced from:
https://www.geeksforgeeks.org/python-membership-identity-operators-not-not/

Using the max() function for the winner, was referenced from:
https://www.w3schools.com/python/ref_func_max.asp

Using the get method within a key (key= .get), also as part of the code to find the winner, 
was referenced from:
https://blog.finxter.com/how-to-get-the-key-with-the-maximum-value-in-a-dictionary/
