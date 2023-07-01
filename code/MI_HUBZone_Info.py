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

