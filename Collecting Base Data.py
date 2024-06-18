import requests
from bs4 import BeautifulSoup
import brotli
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


#url = "https://wattever.com.au/compare-best-electricity-rates-vic/#powercor"

#r = requests.get(url)

#save_html(r.content,"energy_data1")

html = open_html("energy_data1")


soup = BeautifulSoup(html,'html.parser')
data = []

rows = soup.select('#table_8 tbody tr')

for i in rows:
    d = {}
    info= i.select('td')
    d["Provider Name"] = info[2].text
    print(d["Provider Name"])
    d['Plans'] = []
    Specific_Plan_Link = "https://wattever.com.au" + info[7].select_one('a')['href']
    plan_link = requests.get(Specific_Plan_Link)
    soup1 = BeautifulSoup(plan_link.content,'html.parser')
    plan_rows= soup1.select('.ue-content-text')
    print("inside")
    for i in plan_rows:
        h3_tag = i.select_one('h3')
        if h3_tag is not None: 
            if 'Powercor' in h3_tag.text:
                plan_rows= i.select('tbody tr')
                break
    
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
    if d['Plans']:
        data.append(d)


with open('Electricity-plans.json','w') as f:
    json.dump(data,f)

