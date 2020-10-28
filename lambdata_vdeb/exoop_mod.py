"""Lambdata - a collection of Data Science helper functions
with a class added"""

#accessing libraries through pipenv
import pandas as pd
import numpy as np


class DfEda:
    def __init__(self, df):
        self.df = df
    
    def nv_search(self):
        """Cleans a DF"""
        return (('?:',df.isin(['?']).sum()),
            ('none:',df.isin(['none']).sum()),
            ('null:',df.isin(['null']).sum()),
            ('nan:',df.isin(['nan']).sum()))

    def tvt_split(self):
        """Random Train, Val, Test on a DF"""
        tvt = train, val, test = np.split(df.sample(frac=1), [int(.6*len(df)), int(.8*len(df))])
        return (('Training Set:',train.shape),
            ('Validation Set:',val.shape),
            ('Test Set',test.shape))

census = pd.read_csv("https://raw.githubusercontent.com/VPDeb/DS-Unit-2-Applied-Modeling/master/Build%20Week%20Project/census.csv")

x = DfEda(census)