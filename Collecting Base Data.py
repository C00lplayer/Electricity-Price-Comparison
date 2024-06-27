import requests
from bs4 import BeautifulSoup
import brotli
import csv
import json
from time import sleep

def save_html(html, path):
    """Accepts the html content as `html` and the name of the file 
    to save it in as `path` and saves the html content in current 
    workspace as `path`"""
    with open(path, 'wb') as f:
        f.write(html)

def open_html(path):
    """Accepts the html file name as `path` and returns all it's data"""
    with open(path, 'rb') as f:
        return f.read()

"""
# URL in which the data is do be extracted from
url = "https://wattever.com.au/compare-best-electricity-rates-vic/#powercor"

# Extracts the code for the data to be use
r = requests.get(url)

# Saves the webpage code locally so that you can access it multiple times when testing the code so that our data extraction doesn't impact the website
save_html(r.content,"energy_data1")

# NOTE: these 3 lines of code above only need to be executed once as once you save the webpage there is no need to save it again apart from updating values that exist inside the table
"""
# Opens the code for the webpage that was saved locally
html = open_html("energy_data1")

# Pass the webpage code through BeautifulSoup module so that it returns an object that will be easy to navigate through
soup = BeautifulSoup(html,'html.parser')
data = []

# Selecting the specific portion of the HTML in which the table of data exists
rows = soup.select('#table_8 tbody tr')

# Going through each row of the table and saving the required information
for i in rows:
    d = {}
    info= i.select('td')
    d["Provider Name"] = info[2].text
    d['Plans'] = []
    # As the table also includes a link to further electricity plans, it is saved so that we can scrap that too
    Specific_Plan_Link = "https://wattever.com.au" + info[7].select_one('a')['href']
    
    # Using the link that includes the additional plans, we use the request and BeautifulSoup module to load up that webpage
    plan_link = requests.get(Specific_Plan_Link)
    soup1 = BeautifulSoup(plan_link.content,'html.parser')
    
    # Selecting the specific portion of the HTML in which the table of data exists
    plan_rows= soup1.select('.ue-content-text')
    
    # The previous selection made doesn't narrow the code enough so we go through each table to find the specific one we are looking for
    # which in this case is one about 'Powercor'
    for i in plan_rows:
        h3_tag = i.select_one('h3')
        if h3_tag is not None: 
            if 'Powercor' in h3_tag.text:
                plan_rows= i.select('tbody tr')
                break
    
    # Now we go through each row and extract the specific data about the plans we need
    for j in plan_rows:
        d1 = {}
        plan_info = j.select('td')
        if plan_info[4].text == 'D1':
            d1['Plan Name'] = plan_info[0].text
            d1['General Usage Charge'] = plan_info[6].text[:-1]
            d1['Supply Charge'] = plan_info[12].text[:-1]
            d1['Solar Feed-in'] = plan_info[14].text[:-1]
            d1['Upfront Credit']= plan_info[15].text[1:]
            d1['Reference Price'] = plan_info[17].text
            try:
                d1['Plan Link'] = j.select_one('a')['href']
            except:
                pass
            d['Plans'].append(d1)
    
    # We now append the different plans to the main list of data only if the plans exist
    if d['Plans']:
        data.append(d)


# Saving the plan data locally as a json file so that to analyse the data we don't need to repeatedly scrape the page
with open('Electricity-plans.json','w') as f:
    json.dump(data,f)


# Saving the plan data locally as a csv file which is also sorted so that to analyse the data we don't need to repeatedly scrape the page
csv_file = open("master-list-plans.csv","w")
writer = csv.writer(csv_file)

All_Plans = []
for each_provider in data:
    Name = each_provider["Provider Name"]
    
    for plan in each_provider["Plans"]:
        Plan_info = {}
        Plan_info["Provider"] = Name
        Plan_info["Plan Name"] = plan["Plan Name"]
        
        Plan_info["General_Usage"] = plan['General Usage Charge']
        Plan_info["Supply_Charge"] = plan['Supply Charge']
        Plan_info["Upfront Credit"] = plan["Upfront Credit"]
        
        try:
            Plan_info["Link"] = plan["Plan Link"]
        except KeyError:
            Plan_info["Link"] = 'Error: No Link Found'
        
        All_Plans.append(Plan_info)

All_Plans = sorted(All_Plans, key = lambda x: (float(x["General_Usage"]),float(x["Supply_Charge"]),int(x["Upfront Credit"])))

writer.writerow(['Provider','Specific Plan Name', "General_Usage","Supply_Charge",'Upfront Credit',"Link"])

for plan in All_Plans:
        Prover_Name = plan["Provider"]
        Plan_Name = plan["Plan Name"]
        General_Usage = plan['General_Usage']
        Supply_Charge = plan['Supply_Charge']
        Upfront_Credit = plan["Upfront Credit"]
        Link = plan["Link"]
        
        writer.writerow([Prover_Name, Plan_Name, General_Usage,Supply_Charge, Upfront_Credit, Link])

csv_file.close()
