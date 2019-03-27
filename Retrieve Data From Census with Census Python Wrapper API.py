#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

from IPython.core.display import HTML
css = open('style-table.css').read() + open('style-notebook.css').read()
HTML('<style>{}</style>'.format(css))

from census import Census
from us import states

#County code that we may need
#PA,42,095,Northampton County,H1
#PA,42,077,Lehigh County,H1
#'B01001_001E' Total Population
#'B01001_002E' Total Male Population
# B01001_026E Total Female Population
# B01001_003E Total!!Male!!Under 5 years
# B01001_004E Estimate!!Total!!Male!! 5  to 9 years
# B01001_005E Estimate!!Total!!Male!!10 to 14 years
# B01001_006E Estimate!!Total!!Male!!15 to 17 years
# B01001A_001E Total white population
# B01001B_001E Total black population

c = Census('f2952ec4c8b852a48fb61df698d4d43206ab3182')
a = c.acs5.get(('NAME', 'B01001_001E', 'B01001_002E', 'B01001_003E', 'B01001_004E', 'B01001_005E', 
            'B01001_006E',   'B01001_026E', 'B01001A_001E', 'B01001B_001E'),
          {'for': 'county: 095', 'in':'state: 42'}, year = 2017)
pd.DataFrame(a)

