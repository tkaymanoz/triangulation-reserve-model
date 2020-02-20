import pandas as pd
import numpy as np
import datetime as dt

path_to_file = "../triangulation-reserve-model/Data/"

def load_claims(path_to_file):
    claim_data = pd.read_csv(f"{path_to_file}sevha mdara.csv")
    return claims_data



def load_exposure():
    pass

def check_data(data,date_columns):
    for i in date_columns:
        data[i] = pd.to_datetime(data[i])
    
    data["Date Check"] = "Error"
    data.loc[data["Date Incurred"] > data["Date of Loss"], "Date Check"] = "OK"
    data.loc[data["Date Incurred"] == data["Date of Loss"], "Date Check"] = "Warning"
    
    return data

def filter_features(data,features_list):
    data = data.filter(items = features_list)


    return data


def get_features(source):
    pass

def validate(loaded_data):
    date = dt.datetime(loaded_data)
    return date



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

