import csv
import matplotlib.pyplot as plt

markers =['X','^','o','s','p','*','D','P','H','.']
Title_font = {'family':'sans-serif','size':30}
Body_font = {'family':'sans-serif','size':20}

# Enter you plan details below:
PAYONTIMEDISCOUNT = "Enter current pay on time discount here"
Current_General = "Enter Current general usage charge here"
Current_Supply =  "EnterCurrent supply charge here"
Current_usage = {"Aug 2023": "Enter usage in KWH" , "Sep 2023": "Enter usage in KWH" ,"Oct 2023": "Enter usage in KWH" , "Nov 2023": "Enter usage in KWH", "Dec 2023": "Enter usage in KWH" ,"Jan 2024":"Enter usage in KWH", "Feb 2024": "Enter usage in KWH", "Mar 2024": "Enter usage in KWH", "Apr 2024": "Enter usage in KWH", "May 2024": "Enter usage in KWH"}
Periods = {"Aug 2023": 31, "Sep 2023": 30,"Oct 2023": 31, "Nov 2023": 30, "Dec 2023": 31,"Jan 2024":31, "Feb 2024": 29, "Mar 2024": 31, "Apr 2024":30, "May 2024":31}


Dates = Periods.keys()
current_cost = []
for i in Dates:
            days = Periods[i]
            usage = CURRENT_USAGE[i]
            current_cost.append(round(((CURRENT_GENERAL*usage)+(days*CURRENT_SUPPLY))*PAYONTIMEDISCOUNT,2))

plt.figure(figsize=(25,13))
plt.title(f"Cost of Current Plan and Alternative Plans Over Time",fontdict= Title_font)
plt.xlabel("Bill Period", fontdict=Body_font)
plt.ylabel("Cost ($)", fontdict=Body_font)
plt.plot(Dates,current_cost, linewidth = 2)

with open('master-list-plans.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    count = -1
    legend_names = ["Current Plan"]
    for row in reader:
        count+=1
        Provider = row["Provider"]
        Plan_Name = row["Specific Plan Name"]
        General_usage= float(row["General_Usage"])
        Supply_charge = float(row["Supply_Charge"])
        
        cost = []
        for i in Dates:
            days = Periods[i]
            usage = Current_usage[i]
            cost.append(round(((General_usage*usage)/100)+((days*Supply_charge)/100),2))
        
        plt.plot(Dates,cost, marker =markers[count],linewidth = 3)
        legend_names.append(f"{Provider + " "+ Plan_Name}")
        if count == 9:
            break 
plt.legend(legend_names,shadow = True )

plt.show()


