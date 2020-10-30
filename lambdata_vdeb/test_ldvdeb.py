"""Using unittest for lambdata_vdeb package"""
import unittest
from exoop_mod import DfEda
import pandas as pd
import numpy as np
import random




class CleanerTest(unittest.TestCase):
    """Testing the Cleaner function to sum up various kinds of NaNs in DF and make 
    train val test splits"""
    def setUp(self):
        """Create three random dataframes to use in test"""
        self.df1= DfEda(pd.DataFrame({'a':[1, 'none', 3,'nan', 5, 2],
                                      'b':[4, 6, 8, '?', 'null', 9]}))
                              
        self.df2= DfEda(pd.DataFrame({'c':[6, 7, 'null', 9, 10, '?', 12, 5, 3, 2, 5],
                                   'd':[3, 5, '?', 2, 'none', '?', 6, 8, 4, 0, 'nan']}))
        self.df3= DfEda(pd.DataFrame(np.random.randint(1, 101, size=(100, 2)), columns= list('ef')))


    def test_nanvalues(self):
        """Testing the nv_search function that will return which forms of 
        nan values are in your dataframe"""
        nan_dict = DfEda.nv_search(self.df1)
        result = {'?': 1, 'none': 1, 'null': 1, 'nan': 1}
        self.assertEqual(nan_dict, result)

        nan_dict2 = DfEda.nv_search(self.df2)
        result = {'?': 3, 'none': 1, 'null': 1, 'nan': 1}
        self.assertEqual(nan_dict2, result)

    def test_tvtsplit(self):
        """Testing to ensure the dataframe is randomly split into 
        an 80/20/20 split for the train/val/test sets"""
        split_df = DfEda.tvt_split(self.df3)
        tvtt = (('Training Set:', (60, 2)), ('Validation Set:', (20, 2)), ('Test Set:', (20,2)))
        self.assertEqual(split_df, tvtt)



if __name__ == "__main__":
    unittest.main()