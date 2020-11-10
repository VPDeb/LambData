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
        return (('?:',self.df.isin(['?']).sum().sum()),
          ('none:',self.df.isin(['none']).sum().sum()),
          ('null:',self.df.isin(['null']).sum().sum()),
          ('nan:',self.df.isin(['nan']).sum().sum()))
        #return {'?': self.df.isin(['?']).sum().sum(),
         #   'none': self.df.isin(['none']).sum().sum(),
          #  'null': self.df.isin(['null']).sum().sum(),
          #  'nan': self.df.isin(['nan']).sum().sum()}

    def tvt_split(self):
        """Random 80/20/20 Train, Val, Test splits on a DataFrame.
        Also returns the shape of each split"""
        tvt = train, val, test = np.split(self.df.sample(frac=1), [int(.6*len(self.df)), int(.8*len(self.df))])
        return (('Training Set:', train.shape), 
        ('Validation Set:', val.shape), 
        ('Test Set:', test.shape))

census = pd.read_csv("https://raw.githubusercontent.com/VPDeb/DS-Unit-2-Applied-Modeling/master/Build%20Week%20Project/census.csv")

x = DfEda(census)
x.nv_search()