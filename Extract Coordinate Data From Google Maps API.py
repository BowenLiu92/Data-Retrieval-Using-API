#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import googlemaps

#My keyID  AIzaSyAgaUJgH1LLvEww8rQ7dOFg1W2IyDcKDHM

import pandas as pd

# Set Google Maps API key

my_google_maps_key = googlemaps.Client(key = 'Put in your KEY here')

# The table including the addresses whose lat, long data you want to retrieve

df = pd.read_csv('file:///\\Fileserver01\d_drive\lvpcprojects/FutureLV\Shopping%20Centers\SWLehigh%20Southern%20Tier%20Shopping%20Centers.csv')[['LOCATION']]


df['LAT'] = None
df['LON'] = None

for i in range(len(df)):
    geocode_result = my_google_maps_key.geocode(df.iat[i, 0])
    try:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lng"]
        df.iat[i, df.columns.get_loc("LAT")] = lat
        df.iat[i, df.columns.get_loc("LON")] = lon
    except:
        lat = None
        lon = None

