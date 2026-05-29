"""
Assume we have 10 US dollars & 25 Saudi Riyals. Write a Python Script to convert the total currency to Nepali Rupees. (Exchange rates: 1 US Dollar = 133.72 NRs and 1 Saudi Riyal = 35.82 NRs)
Currency in NRs
US Dollars: 10
Saudi Riyals: 25
Total Currency in NRs: 2232.7
"""

doller = 10
riyal = 25
nepali_rupees = (doller * 133.72) + (riyal * 35.82)
print(f"Total currency in NRs: {nepali_rupees}")