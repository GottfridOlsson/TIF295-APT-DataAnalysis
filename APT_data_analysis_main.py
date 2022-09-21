##=======================================================##
##     Project: Atomic Probe Tomography [TIF295]
##        File: APT_data_analysis_main.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-09-21, 13:18
##     Updated: 2022-09-21, 13:18
##       About: Analysis of data from APT lab.
##              1. Read CSV files with Cr-RDF
##              2. Normalize Cr-RDF
##              3. Find wavelength (first max of Cr-RDF)
##              4. Linear fit to find amplitude
##=======================================================##


#---------------#
#    IMPORTS    #
#---------------#

import pandas as pd
import os

#-------------------#
#   HELP FUNCTIONS  #
#-------------------#

CSV_DELIMITER = ','


def read_CSV(read_file_path):
    return pd.read_csv(read_file_path, sep=CSV_DELIMITER)

def get_header_CSV(CSV_data):
    return CSV_data.columns.values



#------------#
#    MAIN    #
#------------#
 
CURRENT_PATH  = os.path.abspath(os.path.dirname(__file__))
CSV_PATH_10h  = '\Data from lab\RDF_10h_removedPole_dist10nm_step0,2nm_bulkNormalizedConc.csv'
CSV_PATH_100h = '\Data from lab\RDF_100h_removedPole_dist10nm_step0,2nm_bulkNormalizedConc.csv'

CSV_10h  = read_CSV(CURRENT_PATH + CSV_PATH_10h)
CSV_100h = read_CSV(CURRENT_PATH + CSV_PATH_100h)
print(CSV_10h, CSV_100h)
