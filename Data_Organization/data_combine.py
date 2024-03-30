import csv
import json

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
year_start = 1960

# Input and output filenames
filepath = '.\Data_Organization\\'
json_file = f'{filepath}data.json'

data = {}  # Initialize empty dictionary to store data
CPI_Data = open(f'{filepath}CPI_Data.csv', 'r', encoding='utf-8-sig')
Unemployment_Data = open(f'{filepath}Unemployment_Data.csv', 'r', encoding='utf-8-sig')
FedFunds_Data = open(f'{filepath}FedFunds_Data.csv', 'r', encoding='utf-8-sig')

CPI_Reader = csv.DictReader(CPI_Data)
Unemploy_Reader = list(csv.DictReader(Unemployment_Data))
FedFunds_Reader = list(csv.DictReader(FedFunds_Data))

next(CPI_Reader)
unem_idx = 12 #For Unemployment (1960 starts at idx 12), increaes by 1 for each year
fed_idx = 66 #for FedFunds, increases by 1 for each month

for row in CPI_Reader: # CPI data extends further back
    year = int(row['Year'])
    if(year < year_start):
        continue

    u_row = Unemploy_Reader[unem_idx] #Unemployment row

    year_data = {}
    for i in range(12):
        month_name = months[i]
        if(len(row[month_name]) == 0):
            break
        f_row = FedFunds_Reader[fed_idx] #FedFunds row
        print(f_row)
        year_data[month_name] = {}
        
        year_data[month_name]['CPI'] = float(row[month_name])
        year_data[month_name]['Unemployment'] = float(u_row[month_name])
        year_data[month_name]['FedFunds'] = float(f_row['FEDFUNDS'])
        fed_idx+=1

    data[year] = year_data
    unem_idx+=1

# Write JSON data to file
with open(json_file, 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

