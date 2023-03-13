import os
import csv
total_months = 0
total_PnL= 0
csvlst =[]
differences = []
file = os.path.join("resources","budget_data.csv")
monthlst =[]


with open(file,"r") as csvpath:
    csvreader = csv.reader(csvpath, delimiter=",")
    next(csvreader, None)
    #we skipped the header to avoid interacting with strings. We've also opened the file and set up empty lists and variables to manipulate
    for line in csvreader:
        csvlst.append(line)
        csvlst
x = range(len(csvlst))
#For a variety of reasons too complicated to explain, directly iterating through this list while using the accumulator value throws up alot
#of errors because we can eventually end up forcing the code to interact with an index in a list which does not exist. the for loop
#allows us to go through the indexs of the rows and the row directly afterwards 
icount =0   
accumulator=0
monthcount=len(csvlst)
for i in x:
    if icount <= 84:
        #we can only run this section of code until 84 because once we are at the last row, the accumulator makes the code look for
        #the next row of this list, since there are no more rows it throws up an error.
        accumulator = accumulator+1
        #this accumulator allows us to create an index that is directly after the current row, we then use it to gather the P/L value in
        #the next row so we can find the change per row, and then append that to a list of values seperate from the other list while keeping track of months
        currentiteration = [sub for sub in csvlst[i]]
        nextiteration= [sub for sub in csvlst[accumulator]]
        newvalue=int((nextiteration[1]))-int((currentiteration[1]))
        differences.append(newvalue)
        monthlst.append(nextiteration[0])
        icount =icount +1
        total_PnL=total_PnL+ int(currentiteration[1])
    elif icount > 84:
        #this is to get the last value which is excluded from the above if statement so we can add it into our "total" profits and losses
        currentiteration = [sub for sub in csvlst[i]]
        total_PnL=total_PnL+ int(currentiteration[1])
#Since we have to seperate the values from the list in order to easily find the data without creating errors from manipulating ints and strings
# we now have to re-unify the differences and the months in order to iterate through this new list and print out the correct month and p/l value

completetuple = zip(monthlst,differences)
completelst =[]
print("Total Months "+ str(monthcount))
print("Total ",str(total_PnL))
print("Average Change "+str(sum(differences)/len(differences)))
for row in completetuple:
    completelst.append(row)
#The below code looks through the profit/loses value in the rows, converts them to integers
#and prints out the entire row once the profit/lost column is equal to the min or max value
for row in completelst:
    if int(row[1])==max(differences):
        print("Greatest Increase in Profits ",row)
    if int(row[1])==min(differences):
        print("Greatest Decrease In ",row)
