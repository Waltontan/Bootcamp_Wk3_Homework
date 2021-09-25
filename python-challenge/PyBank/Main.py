import csv
import os

filepath = os.path.join("Resources","budget_data.csv")


# Open csv file
with open(filepath, "r") as file:
    csvreader = csv.reader(file,delimiter=",")
    
    # write column header into 'header'
    header = next(csvreader)

    # Create a month and profits list from CSV
    months=[] 
    profits = []
    x=0
    
    # Creates a 'months' list to store all date of entries and store the profits in a different list 'profits'
    for rows in csvreader:
        months.append(rows[0]) # Adding every row in date column to the 'months' list
        profits.append(int(rows[1])) # Adding every row in profit column to the 'profits' list
        x=x+1


    # Find net profit for the period
    netpf=0
    for pf in profits:
        netpf = netpf + int(pf) # Adding profits and losses on each row to find total profit



    # Create new list for difference column. The first value is zero
    currentmonth = 0
    nextmonth = 0
    difference = []

    for change in profits:
        if currentmonth != 0: # For each subsequent month the value is not 0 use the below code to find the difference and add it to the 'difference' list
            nextmonth = change
            delta = nextmonth - currentmonth
            difference.append(delta)
            currentmonth = nextmonth

        else: #difference can only be calcualted from 2nd month onwards use this else statement to force 0 into the first value of the 'difference' list
            difference.append(currentmonth)
            currentmonth = change

    # Find the average difference throughout the years 
    netdifference = 0

    for change in difference:
        netdifference = netdifference + change # Loop through all values in 'difference' list and sum it up to find the total difference in the period
    
    averagedelta = round((netdifference / (len(profits)-1)),2) # Find the average different rounded to 2 decimal places

    # Find greatest increase
    greatestincrease = 0
    gidate = ""
    for gi in difference: 
        if gi > greatestincrease: # Only override 'greatestincrease' when the value in the list is more
            greatestincrease = gi
            gidate = months[(difference.index(greatestincrease))] # Index position of the increase and find the corresponding month in the 'months' list
    
    # Find greatest decrease
    greatestdecrease = 0
    gddate = ""
    for gd in difference:
        if gd < greatestdecrease: # Only override 'greatestincrease' when the value in the list is less
            greatestdecrease = gd
            gddaate = months[(difference.index(greatestdecrease))] # Index position of the decrease and find the corresponding month in the 'months' list
    

    print("----------------------------")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {x}")
    print(f"Total: ${netpf}")
    print(f"Average Change: ${averagedelta}")
    print(f"Greatest Increase in Profits: {gidate} (${greatestincrease})")
    print(f"Greatest Decrease in Profits: {gddaate} (${greatestdecrease})")
    print("----------------------------")


# Specifying output location and name of new text file
output_path = os.path.join("Analysis","Financial_Analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as file:

    #write into text file
    file.write("----------------------------")
    file.write('\n')
    file.write("Financial Analysis")
    file.write('\n')
    file.write("----------------------------")
    file.write('\n')
    file.write(f"Total Months: {x}")
    file.write('\n')
    file.write(f"Total: ${netpf}")
    file.write('\n')
    file.write(f"Average Change: ${averagedelta}")
    file.write('\n')
    file.write(f"Greatest Increase in Profits: {gidate} (${greatestincrease})")
    file.write('\n')
    file.write(f"Greatest Decrease in Profits: {gddaate} (${greatestdecrease})")
    file.write('\n')
    file.write("----------------------------")
    file.write('\n')