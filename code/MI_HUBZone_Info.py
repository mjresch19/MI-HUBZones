import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from collections import OrderedDict
import regex as re
import requests
from bs4 import BeautifulSoup

michigan_data = pd.read_excel("datasrc/HUBZone_Counties_MI.xlsx")
cities_and_counties = pd.read_excel("datasrc/USCityCountyList.xlsx", dtype={"county_fips": str})
michigan_HUBZone_info = pd.read_excel("datasrc\Hubzone_FY_2008_2022.xlsx", sheet_name="All_years_MI")

#create an empty dataframe in which we will export to excel after adding data
tac_df  = pd.DataFrame()

'''
Create a dictionary with cities mapped to each county 
'''

cities = michigan_HUBZone_info.loc[:,"recipient_city_name"]

michigan_county_dictionary = {}
michigan_df = cities_and_counties[cities_and_counties["state_id"] == "MI"]

for index, row in michigan_df.iterrows():
    if row["county_name"] not in michigan_county_dictionary:
        michigan_county_dictionary[row["county_name"]] = [row["city"].upper()]
    else:
        michigan_county_dictionary[row["county_name"]].append(row["city"].upper())

'''
Create a list of all Michigan Counties & add to Dataframe
'''

county_list = []

for key in michigan_county_dictionary.keys():
    county_list.append(key)

county_list.sort()

tac_df["County Name"] = county_list

print("Tst")