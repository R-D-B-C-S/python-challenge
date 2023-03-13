import csv
import os

file = os.path.join("resources","election_data.csv")
with open(file,"r") as csvpath:
        csvreader = csv.reader(csvpath, delimiter=",")
        #next(csvreader, None)
        votecount =0
        charlesvote = 0
        dianavote =0
        blankvotes = 0
        raymonvote = 0
        print(csvreader)
        for line in csvreader:
                #print(line)
                votecount = votecount + 1
                if line[2] == "Charles Casper Stockham":
                        charlesvote = charlesvote +1
                elif line[2] == "Diana DeGette":
                        dianavote = dianavote +1
                elif line[2] == "Raymon Anthony Doane":
                        raymonvote = raymonvote+1
                else:
                        blankvotes=blankvotes + 1
                #this section should determine the victor by 
                if charlesvote > dianavote and raymonvote:
                        winner = "Charles Casper Stockham"
                elif dianavote > charlesvote and raymonvote:
                        winner ="Diana DeGette"
                else:
                        winner ="Raymon Anthony Doane"
        print("Total Votes "+ str(votecount))
        print("Charles Vote Count "+str(charlesvote/votecount)+" "+str(charlesvote))   
        print("Diana Vote Count "+ str(dianavote/votecount)+" "+ str(dianavote))           
        print ("Raymon Vote Count "+str(raymonvote/votecount)+" "+str(raymonvote))
        print("Winner "+str(winner))




