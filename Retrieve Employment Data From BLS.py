#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Lehigh County unemployment rate series ID: LAUCN420770000000003
# Lehigh County unemployment series ID: LAUCN420770000000004
# Lehigh County employment series ID: LAUCN420770000000005
# Lehigh County labor force series ID: LAUCN420770000000006
# Northampton County unemployment rate series ID: LAUCN420950000000003
# Northampton County unemployment series ID: LAUCN420950000000004
# Northampton County employment series ID: LAUCN420950000000005
# Northampton County labor force series ID: LAUCN420950000000006
# Pennsylvania unemployment rate series ID: LASST420000000000003
# Pennsylvania unemployment series ID: LASST420000000000004
# Pennsylvania employment series ID: LASST420000000000005
# Pennsylvania labor force series ID: LASST420000000000006


# The code below is to extract population and employment datasets from the new bls data site
import pandas as pd
import json
import requests

headers = {'Content-type': 'application/json'}
extract_list = []
Total_List = ['LAUCN420770000000003', 'LAUCN420770000000004', 'LAUCN420770000000005', 'LAUCN420770000000006',
             'LAUCN420950000000003', 'LAUCN420950000000004', 'LAUCN420950000000005', 'LAUCN420950000000006',
             'LASST420000000000003', 'LASST420000000000004', 'LASST420000000000005', 'LASST420000000000006']
data = json.dumps({"seriesid": Total_List,"startyear":"2016", "endyear":"2017", "annualaverage":True, 
                   "registrationkey":"ffb1aa39d0e04099865528d0ca8e3b20"})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
try:
    df = pd.DataFrame()
    for series in json_data['Results']['series']:
        df_initial = pd.DataFrame(series)
        series_col = df_initial['seriesID'][0]
        for i in range(0, len(df_initial)):
            df_row = pd.DataFrame(df_initial['data'][i])
            df_row['seriesID'] = series_col
            if 'code' not in str(df_row['footnotes']): 
                df_row['footnotes'] = ''
            else:
                df_row['footnotes'] = str(df_row['footnotes']).split("'code': '",1)[1][:1]
            df = df.append(df_row, ignore_index=True)
    df.to_csv('Penn LC NC Employment.csv', index=False)
except:
    json_data['status'] == 'REQUEST_NOT_PROCESSED'
    print('BLS API has given the following Response:', json_data['status'])
    print('Reason:', json_data['message'])

