# First we will import the .csv file to the script..
import csv
from collections import Counter
#import the os of running the code on all the operating system
import os
count = []
#Read the csv file for the location into the script
csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile)
    vote = Counter(count)
    #For printing the object of the csv.reader file use below code.....
    #print(csvreader)
    
    csv_header= next(csvreader) # For skiping the header name of the file....
   
    #If you want to print the header of the sheets below is the code....
    #print(f'csv header: {csv_header}')
    
    #For the total analysis printing part.....
    print("Election Results")
    print("---------------------------------------------------------")
    row = list(csvfile)
    #print(row)     # FOr printing the whole .csv file list....
    #total = sum(csvfile)
    for row in csvfile:
        if row[2] == 'Khan':
            count += 1
        print(count)

    print(f'Total Votes: {len(row)}')    #Print the total months in the output...
    print("---------------------------------------------------------")
    
    