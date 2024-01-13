#Declare / Import the dependencies
import os
import csv

#Specify the path to the CSV file budget_data.csv
budgetData_csv = os.path.join("Resources", "budget_data.csv")

#open and read the data of the CSV file.
with open(budgetData_csv) as data:

    #initiate the reader
    reader = csv.reader(data, delimiter = ",")

    #skip the header row when looping through the data
    header = next(reader)

    #--------------------------------------------------
    #-----------         L  O  O  P         -----------
    #--------------------------------------------------

    #Variables for the amounts to calculate. Must start from 0
    totalMonths = 0
    total = 0
    profit_loss1 = 0

    #Create an empty list for the changes
    changes = []

    #Create Greatest Increase Dictionary, Keys: Date and Amount
    #To find the maximum value in the dataset use float("-inf")
    greatestInc = {"date": "", "amount": float("-inf")}

    # Create Greatest Decrease Dictionary, Keys: Date and Amount
    #To find the minimum value in the dataset use float("inf")
    greatestDec = {"date": "", "amount": float("inf")}

    #Start your loop over the rows to make calculations
    for row in reader:

        #-----------------------------------------------
        #----------        Conditionals        ---------
        #-----------------------------------------------

        #Calculate totalMonths
        totalMonths += 1

        #Calculate total
        total += int(row[1])

        #Create conditionals to calculate profit/loss change
        profit_loss2 = int(row[1])
        if totalMonths > 1:
            change = profit_loss2 - profit_loss1
            changes.append(change)

            #Create conditionals for Greatest Increase in profits
            if change > greatestInc["amount"]:
                #Updates the date associated with the greatest increase
                #to the current date (row[0]).
                greatestInc["date"] = row[0]

                #Updates the maximum increase value
                #to the current change value.
                greatestInc["amount"] = change

            #Create conditionals for Greatest Decrease in profits
            if change < greatestDec["amount"]:
                # Updates the date associated with the greatest decrease
                #to the current date (row[0]).
                greatestDec["date"] = row[0]

                #Updates the minimum increase value
                #to the current change value.
                greatestDec["amount"] = change

        #Profit/loss variables for calculations
        profit_loss1 = profit_loss2

        #Average change calculation // Avoid division by zero
        #len for lenght and != not equal to
        if len(changes) != 0:
            averageChange = round(sum(changes)/ len(changes), 2)
        else:
            averageChange = 0

        #Print the outcomes in a newly created function
        def print_financialAnalysis(totalMonths, total, averageChange, greatestInc, greatestDec):
            print("Financial Analysis")
            print("----------------------------")
            print(f"Total Months: {totalMonths}")
            print(f"Total: ${total}")
            print(f"Average Change: ${averageChange}")
            print(f"Greatest Increase in Profits: {greatestInc["date"]} (${greatestInc["amount"]})")
            print(f"Greatest Decrease in Profits: {greatestDec["date"]} (${greatestDec["amount"]})")


print_financialAnalysis(totalMonths, total, averageChange, greatestInc, greatestDec)

#--------------------------------------------------------------------------
#------       Printing the resulting analysis into a text file       ------
#--------------------------------------------------------------------------

#Specify the output file path
output_path = os.path.join("analysis", "PyBank_analysis.txt")

# Open the file in write mode and redirect the print statements to the file
with open(output_path, "w") as textfile:

    #Inicialize the txt.writer functointo write the variable we created, with a comma delimeter
    csvwriter = csv.writer(textfile)

    #csvwriter.writerow(print_financialAnalysis(totalMonths, total, averageChange, greatestInc, greatestDec))
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {totalMonths}"])
    csvwriter.writerow([f"Total: ${total}"])
    csvwriter.writerow([f"Average Change: ${averageChange}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {greatestInc['date']} (${greatestInc['amount']})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {greatestDec['date']} (${greatestDec['amount']})"])

print(f"Results exported to {output_path}")