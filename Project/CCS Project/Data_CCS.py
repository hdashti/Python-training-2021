#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 12:27:38 2021

@author: Hossein Dashti
Date: 2021-03-05
Title: The carbon emission datasets
"""
import pandas as pd

# Importing Data
raw_data = pd.read_csv("https://github.com/owid/co2-data/raw/master/owid-co2-data.csv")

# Size of the dataframe
# print(raw_data.shape)

# Columns
# print(raw_data.columns)

# Cleaning up, Subsetting data
keep = ['iso_code', 'country', 'year', 'population', 'gdp', 'co2','methane',
        'nitrous_oxide', 'consumption_co2_per_gdp']
data = raw_data[keep]

# Ignore early patchy data
data = data[data.year >= 1900]
# Check code
# print(min(data.year))

# Cleaning up, Remove the "total data" and "na countries"
data = data[(data.iso_code != "OWID_WRL") & (data.iso_code.notna())]

# Adding columns

"""
Calculate the sum of the greenhouse gas emissions, CO2 + Methane + nitrous
oxide
Calculate the CO2 eqivalent emitted per capita (CO2e)
Calculate GDP per capita
"""
data['co2e'] = data[["co2", "methane", "nitrous_oxide"]].sum(axis=1)
data["co2e_pc"] = data.co2e / data.population
data["gdp_pc"] = data.gdp / data.population


# Merging tables and datasets
""" 
We want to add the countries' Social Progress Index (SPI) to our dataset.
Reference: https://www.socialprogress.org/
"""
spi = pd.read_csv("/home/hossein/Downloads/CCS project/2011-2020-Social-Progress-Index.csv")
#spi = spi[("spi.SPI country code" != "WWW")]
#spi = spi[spi. >= 1900]

#Merge two columns
data_all = pd.merge(data, spi,
                      how = "left",
                      left_on = ["iso_code", "year"],
                      right_on = ["SPI country code", "SPI year"])

keep_1 = keep = ['iso_code', 'country', 'year', 'population', 'gdp', 'co2','methane',
        'nitrous_oxide', 'consumption_co2_per_gdp', 'SPI Rank']

data_all = data_all[keep_1]







































