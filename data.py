import pandas as pd
import numpy as np
import datetime as dt


def load_claims():
    pass

def load_exposure():
    pass

def check_data():
    pass

def filter_features(features_list):
    pass


def get_features(source):
    pass

def validate(loaded_data):
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

#checks on integrity of a claims
#1. claim key has a single date of loss
#2. all incurred/paid dates are on or after the date of loss
#3. The total paid amounts should be >=0
#4. Total incurred claim should be the same
#5. Claim amount for single claim should be less than the sum insured
#6 usaite zvekutamba

def iri_function_ndera_tinaye_iri():
    pass