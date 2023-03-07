#################file read-in script############
############Author: Ashley Cale ###########
##########Date:2.23.23#############

#####This script:
##1) reads in textfiles
##2) determine unique points (only need one point for each fire)
##3) makes a panda dataframe that plays nice with google earth engine features 

##Load needed modules  
import os
import ee
import numpy as np
import pandas as pd
ee.Initialize()

###NOTE this will only work if you have a google earth engine account (free) and you have authenticated it in this conda environment##

##This reads in a .txt file##
##make sure you're in the correct directory
def readin_single(file_name):
    allpoints=list()
    with open(file_name, 'r') as _i_:
        for line in _i_:
            line = line.strip('\n')
            line = line.split(',')
            allpoints.append(line)
        del(allpoints[0])
    return(allpoints)

##changing directory         
path='/Users/ashley/Documents/GitHub/fuel_extractions_gee/test.data'
os.chdir(path)   

txt2019=readin_single('2019_combo.txt')
print(txt2019[-1]) ##prints first line

###Determine the unique fire ID's###
def unique_vals(raw_data):
    most_recent = list()
    points= list()
    for sub in raw_data:        
        if sub[1] not in most_recent:
            print(sub[1])
            most_recent.append(sub[1])
            points.append(sub)
        else:
             pass
    return(points)

unq2019= unique_vals(txt2019) 
print(unq2019[-1])
len(unq2019)


df2019= pd.DataFrame(unq2019, columns = ["date","fireID","fire_len","pm_sum_fire_ug","ba_sum_fire","pm_sum_day","ba_sum_day","heat_sum_day","day_lat","day_lon"])
len(df2019) 
