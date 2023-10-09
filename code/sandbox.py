# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 19:56:05 2023

@author: Davis
"""

import pandas as pd

in_path = "../cluster_data/"

cities = pd.read_csv(in_path + 'cities_' + '4' + '.csv')
scaled = pd.DataFrame()
scaled['Cluster'] = cities['Cluster']
print(scaled[scaled['Cluster']])