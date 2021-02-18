# First we will import the .csv file to the script..
import csv
#import the os of running the code on all the operating system
import os
'''max_v =[]
   min_v =[]'''
#Read the csv file for the location into the script
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile)
    
    #For printing the object of the csv.reader file use below code.....
    #print(csvreader)
    
    csv_header= next(csvreader) # For skiping the header name of the file....
   
    #If you want to print the header of the sheets below is the code....
    #print(f'csv header: {csv_header}')

    #For the total analysis printing part.....
    print("Final Analysis")
    print("---------------------------------------------------------")

    row = list(csvfile)
    
    #total = sum(csvfile)
    print(f'Total Months: {len(row)}')    #Print the total months in the output...
    
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    total = 0
     
    csv_header= next(csvreader) #Skipping the header row or the first row of the .csv file....
    
    
    total = sum(int(row[1]) for row in csvreader)    # For summing the Total Profit/Losses... 
    print(f'Total Profit/Losses is: $ {total}')  # Print the Total Profit/Losses...
    
    
with open(csvpath) as csvfile:
    #define variables
    rowcount = 0
    first_value = 0
    next_value = 0
    average = 0 
    great_increase =0
    great_month = 0
    great_decrease = 0
    low_month = 0
    change = 0
    total_change = 0 
    csvreader  =csv.reader(csvfile)
    csv_header = next(csvreader)
    

    for row in csvreader:
        rowcount += 1 #count row another method
        #max_v.append (float(row[1])) #To list the maximun value of the Profit/losses column
        #min_v.append (float(row[1])) # To list the minimum value of the Profit/losses column
        
        if first_value == 0: #For taking the first value of column..
            first_value = int(row[1])

        else:
            next_value = int(row[1])    #select the next value in the column..
            change = next_value - first_value   #Get the change in Profit/Losses for a period of a month
            total_change = change + total_change    #Get the total change in Profit/Losses for the entire data.

            if great_increase < change:     #Check for the greatest increase in Profit..
                great_month = row[0]    #Get the month of the Greatest Profit..
                great_increase = change # Save the greatest change into a variable.. 

            if great_decrease > change: #Check for the greatest loss..
                low_month = row[0]  #Get the month with greatest loss..
                great_decrease = change #Save the greatest loss into a variable...
            first_value = next_value #Check if the first value and next value are same stop the loop..

    print(f'The Total Change in Profit is: $ {total_change}')    #Print the Total change..
    #print(change)
    average = round(total_change/(rowcount-1),2) #Get the average of the Total Profit/Losses..
    print(f'The average change is: $ {average}') #Print the average change..
    print (f'The Greatest increase in Profit: {great_month} , $ ({great_increase})') #Print the greatest profit along with its month..
    print(f'The Greatest decrease in Profit: {low_month}, $ ({great_decrease})') #Print the greatest loss along with its month..
    '''print(f'The Maximun Profit/Losses {max(max_v)}')
    print(f'The Minimum Profit/Losses {min(min_v)}')''' #Extra Work for Minimum and MAximum Values form the PRofit/Losses Column..

# For Printing the output into the text file..
output_path = os.path.join('Resources','output.txt')

with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Final Analysis \n")
    txtfile.write("--------------------------------------------------------- \n")
    txtfile.write(f'Total Months: {rowcount} \n')
    txtfile.write(f'Total Profit/Losses is: $ {total} \n')
    txtfile.write(f'The Total Change in Profit is: $ {total_change} \n')
    txtfile.write(f'The average change is: $ {average} \n')
    txtfile.write(f'The Greatest increase in Profit: {great_month} , $ ({great_increase}) \n')
    txtfile.write(f'The Greatest decrease in Profit: {low_month}, $ ({great_decrease}) \n')
