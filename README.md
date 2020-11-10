# LambData
Lambda Journey Starting at Unit3
Creating a package in Sprint1


Class DfEda was created for simulataneous download of nv_search and tvt_split.

nv_search: scans the dataframe for the most used values for nan ('?', 'none', 'null', & 'nan').
        Returning what kind it is and what column it is in.

tvt_split: easily takes the dataframe and splits it into an 80/20/20 split to have a train/validation/test
        set to work with for your machine learning projects.  It will also print the shape of each split set.