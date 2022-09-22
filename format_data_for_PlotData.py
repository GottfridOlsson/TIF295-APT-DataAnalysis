##=======================================================##
##     Project: Atomic Probe Tomography [TIF295]
##        File: format_data_for_PlotData.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-09-22, 18:52
##     Updated: 2022-09-22, 18:52
##       About: Analysis of data from APT lab.
##              1. Read CSV files with Cr-RDF
##              2. Format data to plot with PlotData.py
##              3. Export formatted CSV
##=======================================================##


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


# READ CSV #
CURRENT_PATH  = os.path.abspath(os.path.dirname(__file__))
FORMATTED_CSV_PATH = CURRENT_PATH + '\Formatted data for PlotData\RDF_removedPole_dist10nm_step0,2nm_bulkNormalizedConc_10h_100h_Cr.csv'

CSV_PATH_10h  = '\Data from lab\RDF_10h_removedPole_dist10nm_step0,2nm_bulkNormalizedConc.csv'
CSV_PATH_100h = '\Data from lab\RDF_100h_removedPole_dist10nm_step0,2nm_bulkNormalizedConc.csv'

CSV_10h  = read_CSV(CURRENT_PATH + CSV_PATH_10h)
CSV_100h = read_CSV(CURRENT_PATH + CSV_PATH_100h)

header_10h  = get_header_CSV(CSV_10h)
header_100h = get_header_CSV(CSV_100h)


# PICK OUT DISTANCE AND (BULK NORMALIZED) Cr CONCENTRATION #
distance_10h  = CSV_10h[header_10h[0]]
distance_100h = CSV_100h[header_100h[0]] 

Cr_conc_10h  = CSV_10h[header_10h[2]]
Cr_conc_100h = CSV_100h[header_100h[2]]


# ARRANGE AND EXPORT DATA FOR PLOTDATA #
data = {'Distance (nm)': distance_10h, 'Cr (10h, bulk normalized concentration ionic percent)': Cr_conc_10h, 'Cr (100h, bulk normalized concentration ionic percent)': Cr_conc_100h}
df = pd.DataFrame(data)
df.to_csv(FORMATTED_CSV_PATH, sep=CSV_DELIMITER, index=False)

print(f"Successfully formatted and exported data to: {FORMATTED_CSV_PATH}")