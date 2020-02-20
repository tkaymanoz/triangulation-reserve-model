import pandas as pd
import numpy as np
import datetime as dt
import sys

path_to_file = "../triangulation-reserve-model/Data/"

def load_data(path_to_file):
    data = pd.read_csv(path_to_file)
    return data

def filter_features(data,features_list):
    '''filter features that are used to generate traingles'''
    data = data.filter(items = features_list)
    return data

def validate_dates(data,date_columns,min_date):
    '''checks if dates are reasonable. returns error message if Date Inccurred < Date of Loss'''
    data = data.loc[data["Date of Loss"] >= pd.to_datetime(min_date)]
    
    for i in date_columns:
        data[i] = pd.to_datetime(data[i])
    
    data["Date Check"] = "Error"
    data.loc[data["Date Incurred"] > data["Date of Loss"], "Date Check"] = "OK"
    data.loc[data["Date Incurred"] == data["Date of Loss"], "Date Check"] = "Warning"
    if len(data.loc[data["Date Check"] == "Error"]) > 0:
        sys.exit("There are some observations with Date Incurred greater than Date of Loss")
        
    return data

def validate_incremental_claims(loaded_data):
    '''checks if the aggredate claims per claim key are negative'''
    loaded_data["Incremental Claim Amount"] = pd.to_numeric(loaded_data["Incremental Claim Amount"],errors = "coerce")
    claims_check = loaded_data.groupby(["Claim Key"])["Incremental Claim Amount"].agg("sum")
    claims_check = pd.DataFrame(claims_check)
    claims_check["Claims Check"] = "error"
    claims_check.loc[claims_check["Incremental Claim Amount"] >= 0 , "Claims Check"] = "ok"

    if len(claims_check.loc[claims_check["Claims Check"] == "error"]) > 0:
        sys.exit("some claim keys have have an aggregate less then 0")
    
    return claims_check


def load_exposure():
    pass

def get_features(source):
    pass

#date checks
def is_date_greater_or_equal(first_date,second_date):
    #use datetime module
    pass

def is_valid_date(date_value):
    pass

#checks on the data format
#1. we expect certain column names in our data. if those are missing, 
#   hapana zvatiri kuita
#   alternative is to allow user to define which column is doing what after upload. But this feels convoluted and painful to code
#2. we expect certain columns to have specific data types
#use try except


#checks on integrity of a claims
#1. claim key has a single date of loss
#2. all incurred/paid dates are on or after the date of loss
#3. The total paid amounts should be >=0
#4. Total incurred claim should be the same
#5. Claim amount for single claim should be less than the sum insured
#6 usaite zvekutamba

def iri_function_ndera_tinaye_iri():
    pass

