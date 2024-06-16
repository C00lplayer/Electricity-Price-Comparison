import requests
from bs4 import BeautifulSoup
import brotli

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
    info.pop(0)
    info.pop(0)
    d["Provider Name"] = info.pop(0).text
    d["Flat Rate"] = info.pop(0).text + "/kWh"
    d["Daily Charge"] = info.pop(0).text
    info.pop(0)
    d["Reference Price"] =info.pop(0).text
    d["Specific Plan Links"] = "https://wattever.com.au" + info.pop(0).select_one('a')['href']
    data.append(d)

print(data[2])

