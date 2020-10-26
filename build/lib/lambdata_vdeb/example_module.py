"""Lambdata - a collection of Data Science helper functions"""

#accessing libraries through pipenv
import pandas as pd
import numpy as np



def df_cleaner(df):
    """Cleans a DF"""
    return (('?:',df.isin(['?']).sum()),
          ('none:',df.isin(['none']).sum()),
          ('null:',df.isin(['null']).sum()),
          ('nan:',df.isin(['nan']).sum()))

def df_split(df):
    """Destroys a DF"""
    tvt = train, val, test = np.split(df.sample(frac=1), [int(.6*len(census)), int(.8*len(census))])
    print(('Training Set:',train.head(1)),
        ('Validation Set:',val.head(1)),
        ('Test Set',test.head(1)))

    