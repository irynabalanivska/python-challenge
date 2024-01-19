#import modules
import os
import csv
#set local pc path to data csv file
csv_path=os.path.join("Resources/election_data.csv")

with open(csv_path,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)
    #set lists
    total_v=[]
    candidate_t=[]
    clear_can=[]
    vote_count = []
    vote_percent = []
    #run through the file
    for row in csvreader:
        total_v.append(int(row[0]))
        total_v_count=len(total_v)
        candidate_t.append(row[2])

    for x in set(candidate_t):
       clear_can.append(x)
       y=candidate_t.count(x)
       vote_count.append(y)
       z=(y/len(candidate_t))*100
       vote_percent.append(z)
   #use index
    max_vote=max(vote_count)
    winner=clear_can[vote_count.index(max_vote)]
    
#print to terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_v_count}")
print("-------------------------")
for i in range(len(clear_can)):
    print(f"{clear_can[i]}: {round((vote_percent[i]),3)}%  ({vote_count[i]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#write csv file
with open("output.txt","wt") as new:
    new.write("Election Results\n")
    new.write("------------------------\n")
    new.write(f"Total Votes: {total_v_count}\n")
    new.write(f"-------------------------\n")
    for i in range(len(clear_can)):
        new.write(f"{clear_can[i]}: {round((vote_percent[i]),3)}%  ({vote_count[i]})\n")
    new.write(f"-------------------------\n")
    new.write(f"Winner: {winner}\n")
    new.write(f"-------------------------\n")