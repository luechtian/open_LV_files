###############################################################################
import os
import glob
import numpy
import pandas as pd
import argparse
###############################################################################
def open_LVfile(LVfile):
    """
    This function opens a single text file, removes redundant columns and renames the columns.
    this function returns cleaner table.
    """
    col_names = list(pd.read_table(LVfile, skiprows=1, usecols = lambda column : 'Unnamed' not in column))
    lipid_data = pd.read_table(LVfile, skiprows=2, index_col=0, usecols = lambda column : column not in ['Sample ID', 'PIS m/z', 'Polarity', 'View Type', '(ScanName)'])
    lipid_data.columns = col_names[1:]
    return lipid_data

###############################################################################
#-----------------------------------------------------------------------------#
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = 'The script gives a headed(5) output of cleaned LipidView-textfiles for each lipidclass.')
    parser.add_argument('LView_file', help = "The filepath for the LipidView text files to clean up. (your\filepath\*.txt)")
    args = parser.parse_args()



    file_location = args.LView_file
    filenames = glob.glob(file_location)

    for i in range(0,len(filenames)):
        F'{headers[col]}' = open_LVfile(filenames[i])
        print(data.head(5))
#-----------------------------------------------------------------------------#
