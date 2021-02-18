# First we will import the .csv file to the script..
import csv
from collections import Counter
#import the os of running the code on all the operating system
import os

#Read the csv file for the location into the script
csvpath = os.path.join('Resources','election_data.csv') #for Total votes using list method
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)

    print("Election Results")
    print("---------------------------------------------------------")
    row = list(csv_file)
    print(f'Total Votes: {len(row)}')    #Print the total votes in the output...
    print("---------------------------------------------------------")
    

with open(csvpath,'r') as csvfile: #for all other Calculation without making a list
    csvreader = csv.reader(csvfile, delimiter= ',')
    # Variable Define..
    count = []
    row_c = 0
    khan_percentage = 0
    correy_percentage = 0
    li_percentage =0
    otooley_percentage = 0 
    #For printing the object of the csv.reader file use below code.....
    #print(csvreader)
    
    csv_header= next(csvreader) # For skiping the header name of the file....
   
    #If you want to print the header of the sheets below is the code....
    #print(f'csv header: {csv_header}')
    #print(row)     # For printing the whole .csv file list....
    #total = sum(csvfile)
    votes = [vote for vote in csvreader] #loop to get the votes..
    
    count = Counter([row[2] for row in votes])  # count the votes each voter has received..
    new_vote = [row + [str(count[row[2]])] for row in votes]    # for getting the voter with the maximun votes and storing the vote count

    # Find the percentage of votes each voter has received..
    khan_percentage = round(((count["Khan"]/len(row)) *100),2)  
    correy_percentage = round(((count["Correy"]/len(row)) *100),2)
    li_percentage = round(((count["Li"]/len(row)) *100),2)
    otooley_percentage = round(((count["O'Tooley"]/len(row)) *100),2)

    # For Displaying each voters received votes and percentage of votes received..
    print(f'Khan: {khan_percentage} % ({count["Khan"]})')
    print(f'Correy: {correy_percentage} % ({count["Correy"]})')
    print(f'Li: {li_percentage} % ({count["Li"]})')
    print(f'O`Tooley: {otooley_percentage} % (', end='')
    print(count["O'Tooley"] , end=''), print(")")
    
    print("---------------------------------------------------------")
    print(f'Winner: {max(new_vote)}')   #Display the winner of the Election along with the County 
    '''In the output you might see that is also show the voter ID as well as the County and the Candidate, 
        Because I was having problem printing only the Candidate name. Hope you can understand'''
    print("---------------------------------------------------------")

# For Printing the output into the .txt file....
output_path = os.path.join('Analysis','PyPoll_Result.txt')

with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Election Results \n")
    txtfile.write("--------------------------------------------------------- \n")
    txtfile.write(f'Total Votes: {len(row)} \n')
    txtfile.write("--------------------------------------------------------- \n")
    txtfile.write(f'Khan: {khan_percentage} % ({count["Khan"]}) \n')
    txtfile.write(f'Correy: {correy_percentage} % ({count["Correy"]}) \n')
    txtfile.write(f'Li: {li_percentage} % ({count["Li"]}) \n')
    txtfile.write(f'O`Tooley: {otooley_percentage} % (')
    txtfile.write(str(count["O'Tooley"]))
    txtfile.write(") \n")
    txtfile.write("--------------------------------------------------------- \n")
    txtfile.write(f'Winner: {max(new_vote)} \n')
    txtfile.write("--------------------------------------------------------- \n")
    
    
    