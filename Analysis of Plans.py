import csv
import matplotlib.pyplot as plt

markers =['X','^','o','s','p','*','D','P','H','.']
Title_font = {'family':'sans-serif','size':30}
Body_font = {'family':'sans-serif','size':20}
PAYONTIMEDISCOUNT = 0.7
Current_General = 0.38874
Current_Supply = 1.87924
Current_usage = {"Aug 2023": 300.745, "Sep 2023": 235.27,"Oct 2023": 226.827, "Nov 2023": 184.793, "Dec 2023": 85.804,"Jan 2024":248.313, "Feb 2024": 256.431, "Mar 2024": 238.438, "Apr 2024":282.162, "May 2024":444.133}
Periods = {"Aug 2023": 31, "Sep 2023": 30,"Oct 2023": 31, "Nov 2023": 30, "Dec 2023": 31,"Jan 2024":31, "Feb 2024": 29, "Mar 2024": 31, "Apr 2024":30, "May 2024":31}


Dates = Periods.keys()
current_cost = []
for i in Dates:
            days = Periods[i]
            usage = Current_usage[i]
            current_cost.append(round(((Current_General*usage)+(days*Current_Supply))*PAYONTIMEDISCOUNT,2))

plt.figure(figsize=(25,13))
plt.title(f"Cost of Current Plan and Alternative Plans Over Time",fontdict= Title_font)
plt.xlabel("Bill Period", fontdict=Body_font)
plt.ylabel("Cost ($)", fontdict=Body_font)
plt.plot(Dates,current_cost, linewidth = 2)

with open('master-list-plans.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    count = -1
    legend_names = []
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


