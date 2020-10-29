"""Using unittest for lambdata_vdeb package"""
import unittest
from exoop_mod import DfEda
import pandas as pd




class CleanerTest(unittest.TestCase):
    """Testing the Cleaner function to sum up various kinds of NaNs in DF"""
    def setUp(self):
        self.df1= DfEda(pd.DataFrame({'a':[1, 'none', 3,'nan', 5, 2],
                                      'b':[4, 6, 8, '?', 'null', 9]}))
                              
        self.df2= DfEda(pd.DataFrame({'c':[6, 7, 'null', 9, 10, '?', 12, 5, 3, 2, 5],
                                   'd':[3, 5, '?', 2, 'none', '?', 6, 8, 4, 0, 'nan']}))

    def test_nanvalues(self):
        self.assertIn(['?'].sum(), self.df1)

#self.df.isin(['?']).sum()



if __name__ == "__main__":
    unittest.main()