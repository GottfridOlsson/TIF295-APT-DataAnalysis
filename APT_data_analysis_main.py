##=======================================================##
##     Project: Atomic Probe Tomography [TIF295]
##        File: APT_data_analysis_main.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-09-21, 13:18
##     Updated: 2022-09-21, 15:50
##       About: Analysis of data from APT lab.
##              1. Read CSV files with Cr-RDF
##              2. Normalize Cr-RDF
##              3. Find wavelength (first max of Cr-RDF)
##              4. Linear fit to find amplitude
##              5. Print values
##=======================================================##


#---------------#
#    IMPORTS    #
#---------------#

import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import linear_regression



#-------------------#
#   HELP FUNCTIONS  #
#-------------------#

CSV_DELIMITER = ','


def read_CSV(read_file_path):
    return pd.read_csv(read_file_path, sep=CSV_DELIMITER)

def get_header_CSV(CSV_data):
    return CSV_data.columns.values

def get_min_value_and_index(list):
    list = np.array(list)
    min_val = list[0]
    min_val_index = 0
    
    for i in range(len(list)):
        if list[i] < min_val:
            min_val = list[i]
            min_val_index = i
    
    return min_val, min_val_index

def amplitude_from_RDF(RDF_0, C_0):
    return 2*C_0*np.sqrt(2*RDF_0-1)



#------------#
#    MAIN    #
#------------#

Plot = True

# READ CSV #
CURRENT_PATH  = os.path.abspath(os.path.dirname(__file__)
)
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



# GET WAVELENGTH FROM RDF #
min_Cr_conc_100h, min_Cr_conc_100h_index = get_min_value_and_index(Cr_conc_100h)
min_distance_100h = distance_100h[min_Cr_conc_100h_index]

max_Cr_conc_100h = np.max(Cr_conc_100h[min_Cr_conc_100h_index:-1])
max_distance_100h = 0
for i, Cr_conc in enumerate(Cr_conc_100h):
    if Cr_conc == max_Cr_conc_100h:
        max_distance_100h = distance_100h[i]

max_Cr_conc_10h = np.max(Cr_conc_10h[17:-1]) #by looking at graph
max_distance_10h = 4.0 #from graph



# ASSIGN AND PRINT VALUES #
lambda_100h = {}
lambda_100h['First maximum'] = max_distance_100h   # [nm]
lambda_100h['First minimum'] = 2*min_distance_100h # [nm]

lambda_10h = {}
lambda_10h['First maximum'] = max_distance_10h   # [nm]

print("\nWavelength determined from RDF (100h):\n  From first maximum: " + str(lambda_100h['First maximum']) + " nm\n  From first minimum: " + str(lambda_100h['First minimum']) + " nm")
print("\nWavelength determined from RDF (10h):\n  From first maximum: " + str(lambda_10h['First maximum']) + " nm")



# AMPLITUDE FOR 100h #
C_0 = [0.35452221537718685, 0.3520788658071025] #from "bulk concentration (ionic %)" of Cr in data files "RDF_*h_removedPole_dist10nm_step0,2nm.csv" from the lab
amplitude = [0,0]
n_first_values = [4, 5] #chosen based on what points of RDF we want to do linear regression to (plot and see)
distance = [distance_10h, distance_100h]
Cr_conc  = [Cr_conc_10h, Cr_conc_100h]

for i in range(2):
    x_data = np.array(distance[i][0:n_first_values[i]])
    y_data = np.array(Cr_conc[i][0:n_first_values[i]])

    m, k = linear_regression.solve_normal_equation(x_data, y_data, degree=1)

    if True:
        x = np.linspace(0,1.5,10)
        y = k*x + m
        plt.plot(distance_10h,  Cr_conc_10h,  marker='o', label='Cr-conc 10h')
        plt.plot(distance_100h, Cr_conc_100h, marker='x', label='Cr-conc 100h')
        plt.plot(x, y,                        marker='s', label='linear least squares fit')
        plt.legend()
        plt.grid()
        plt.show()

    RDF_0 = m #intercept y-axis at x=0
    amplitude[i] = amplitude_from_RDF(RDF_0, C_0[i]) # [nm], = 2*A = 2*C_0*sqrt(2*RDF(0)-1)

print("\nCalculated amplitude for  10h is: " + str(amplitude[0]) + " nm")
print("Calculated amplitude for 100h is: " + str(amplitude[1]) + " nm\n")

# EOF #