import json
import csv

with open('Electricity-plans.json','r') as f:
    data = json.load(f)



# Code for outputting and calculating monthly cost:
"""
print(f"{'Provider':<20} {'Specific Plan Name':<60} {'Estimated Monthly Price':<30} {'Upfront Credit':<20} {"Link":<30}")
print("-"*170)

Monthly_Usage = 282.162
DAYS_IN_A_MONTH= 30

for each_provider in data:
    Name = each_provider["Provider Name"]
    for plan in each_provider["Plans"]:
        Plan_Name = plan["Plan Name"]
        General_Usage = (Monthly_Usage* float(plan['General Usage Charge']))/100
        Supply_Charge = (DAYS_IN_A_MONTH*float(plan['Supply Charge']))/100
        Estimated_Monthly_Price = "$" + str(round(General_Usage + Supply_Charge,2))
        Upfront_Credit =  "$" + plan["Upfront Credit"]
        try:
            Link = plan["Plan Link"]
        except KeyError:
            Link = 'Error: No Link Found'
        print(f"{Name:<20} {Plan_Name:<60} {Estimated_Monthly_Price:<30} {Upfront_Credit:<20} {Link:<30}")

with open("Table-of-Electricity-Prices.json", 'r'):
"""

# Code for outputting and calculating monthly cost which is sorted by cheapest first:
"""
All_Plans = []
Monthly_Usage = 282.162
DAYS_IN_A_MONTH= 30

for each_provider in data:
    Name = each_provider["Provider Name"]
    for plan in each_provider["Plans"]:
        Plan_info = {}
        Plan_info["Provider"] = Name
        Plan_info["Plan Name"] = plan["Plan Name"]
        General_Usage = (Monthly_Usage* float(plan['General Usage Charge']))/100
        Supply_Charge = (DAYS_IN_A_MONTH*float(plan['Supply Charge']))/100
        Plan_info["Estimated Monthly Price"] = "$" + str(round(General_Usage + Supply_Charge,2))
        Plan_info["Upfront Credit"] =  "$" + plan["Upfront Credit"]
        try:
            Plan_info["Link"] = plan["Plan Link"]
        except KeyError:
            Plan_info["Link"] = 'Error: No Link Found'
        All_Plans.append(Plan_info)
All_Plans = sorted(All_Plans, key = lambda x: (float(x["Estimated Monthly Price"][1:]),int(x["Upfront Credit"][1:])))

print(f"{'Provider':<20} {'Specific Plan Name':<60} {'Estimated Monthly Price':<30} {'Upfront Credit':<20} {"Link":<30}")
print("-"*170)
#print(All_Plans)
for plan in All_Plans:
        Prover_Name = plan["Provider"]
        Plan_Name = plan["Plan Name"]
        Estimated_Monthly_Price = plan["Estimated Monthly Price"]
        Upfront_Credit = plan["Upfront Credit"]
        Link = plan["Link"]
        print(f"{Prover_Name:<20} {Plan_Name:<60} {Estimated_Monthly_Price:<30} {Upfront_Credit:<20} {Link:<30}")
"""


All_Plans = []
Monthly_Usage = 282.162
DAYS_IN_A_MONTH= 30
csv_file = open("sorted-monthly-plans.csv","w")
writer = csv.writer(csv_file)


for each_provider in data:
    Name = each_provider["Provider Name"]
    for plan in each_provider["Plans"]:
        Plan_info = {}
        Plan_info["Provider"] = Name
        Plan_info["Plan Name"] = plan["Plan Name"]
        General_Usage = (Monthly_Usage* float(plan['General Usage Charge']))/100
        Supply_Charge = (DAYS_IN_A_MONTH*float(plan['Supply Charge']))/100
        Plan_info["Estimated Monthly Price"] = "$" + str(round(General_Usage + Supply_Charge,2))
        Plan_info["Upfront Credit"] =  "$" + plan["Upfront Credit"]
        try:
            Plan_info["Link"] = plan["Plan Link"]
        except KeyError:
            Plan_info["Link"] = 'Error: No Link Found'
        All_Plans.append(Plan_info)
All_Plans = sorted(All_Plans, key = lambda x: (float(x["Estimated Monthly Price"][1:]),int(x["Upfront Credit"][1:])))

writer.writerow(['Provider','Specific Plan Name', 'Estimated Monthly Price', 'Upfront Credit',"Link"])

for plan in All_Plans:
        Prover_Name = plan["Provider"]
        Plan_Name = plan["Plan Name"]
        Estimated_Monthly_Price = plan["Estimated Monthly Price"]
        Upfront_Credit = plan["Upfront Credit"]
        Link = plan["Link"]
        writer.writerow([Prover_Name, Plan_Name, Estimated_Monthly_Price, Upfront_Credit, Link])

csv_file.close()

#with open("sorted-monthly-plans.csv","r") as csv_file:
     #print(csv_file.read())
