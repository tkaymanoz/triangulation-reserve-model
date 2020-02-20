
import pandas as pd
import datetime as dt
import numpy as np

def get_delays(data):
    '''create delays column from the date incurred and date of loss values'''
    data["Date of Loss Code"] = data["Date of Loss"].dt.year
    data["Date Incurred Code"] = data["Date Incurred"].dt.year
    data["Delays"] = data["Date Incurred Code"] - data["Date of Loss Code"]
    return data

def get_triangles(data):
    '''creates 2 triangles. The second one is a cumulative sum triangle'''
    triangle = pd.crosstab(data["Date of Loss Code"], 
            data["Delays"], data["Incremental Claim Amount"],
            aggfunc="sum",dropna = True, margins= True, margins_name = "Total").round(0)
    triangle = pd.DataFrame(triangle)
    cumsum_triangle = triangle.cumsum(axis = 1)
    return triangle,cumsum_triangle

def save_data(data):
    data.to_csv(data)
