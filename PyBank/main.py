import os
import csv
#set local pc path to data csv file
bank_csv=os.path.join('Resources/budget_data.csv')

with open(bank_csv,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)
    #create empty lists to add the csv values to 

    total_months=[]
    profit=[]
    change_profit=[]   
    #iterate through the values and add them to the empty list 
    for row in csvreader:
       total_months.append(row[0])
       profit.append(int(row[1]))
       sum_months=len(total_months)
       sum_profit=sum(profit)

    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
        
monthly_change=sum(change_profit)/len(change_profit)
#evaluate the max and min from the list made
max_increase=max(change_profit)
max_decrease=min(change_profit)
#using the index
increase_month=total_months[change_profit.index(max_increase)+1]
decrease_month=total_months[change_profit.index(max_decrease)+1]

print("Financial Analysis")
print("------------------------")
print(f"Total Months: {sum_months}")
print(f"Total: ${sum_profit}")
print(f"Average Change : ${round((monthly_change),2)}")
print(f"Greatest Increase in Profits: {increase_month}  (${max_increase})")
print(f"Greatest Decrease in Profits: {decrease_month}  (${max_decrease})")
    
with open("output.txt", "wt") as new:
    new.write("Financial Analysis\n")
    new.write("------------------------\n")
    new.write(f"Total Months: {sum_months}\n")
    new.write(f"Total: ${sum_profit}\n")
    new.write(f"Average Change : ${round((monthly_change),2)}\n")
    new.write(f"Greatest Increase in Profits: {increase_month}  (${max_increase})\n")
    new.write(f"Greatest Decrease in Profits: {decrease_month}  (${max_decrease})\n")
