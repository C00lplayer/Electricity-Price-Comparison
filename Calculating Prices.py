import json

with open('Elec-prices.json','r') as f:
    data = json.load(f)

print(f"{'Provider':<15} {'Specific Plan Name':<25} {'Estimated Monthly Price':<30} {'Upfront Credit':<20} {"Link":<30}")
print("-"*110)

for each_plan in data:
    Name = each_plan["Provider Name"]
