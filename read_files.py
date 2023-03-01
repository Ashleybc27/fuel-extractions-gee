###read in files, I'm using base to make this easier for non py users to potentially use/understand
###Author: Ash Cale 
###Date:2.23.23
import os
import ee
import numpy as np
import pandas as pd
ee.Initialize()

np.__file__

def readin(path):
    files = os.listdir(path)
    #print(files)
    allpoints=list()
    for i in files:
        with open(i, 'r') as _i_:
            for line in _i_:
                line = line.strip('\n')
                line = line.split(',')
                if line[0] != float:
                     pass
                else:
                    allpoints.append(line)
    return(allpoints)


            
path='/Users/ashley/Documents/GitHub/fuel_extractions_gee/test.data'

test=readin(os.getcwd())
print(test)

def unique(test):
    most_recent = list()
    points= list()
    for sub in test:        
        if set([sub[1], sub[0].split('-')[0]]) not in most_recent:
            print(sub[0].split('-')[0])
            print(sub[1])
            most_recent.append(set([sub[0].split('-')[0],sub[1]]))
            points.append(sub)
        else:
             pass
    return(points)

test2= unique(test) 
del(test2[0])
print(test2[0])
test3= pd.DataFrame(test2, columns = ["date","fireID","fire_len","pm_sum_fire_ug","ba_sum_fire","pm_sum_day","ba_sum_day","heat_sum_day","day_lat","day_lon"])
len(test2)  

for index,row in test3.iterrows():
    if row['day_lat'] is int:
        print('sad')
    else:
         pass

features=[]
for index,row in test3.iterrows():
    print(dict(row))
    poi_geometry = ee.Geometry.Point([row['day_lon'],row['day_lat']])
    
    print(poi_geometry)
    poi_properties = dict(row)
    poi_feature = ee.Feature(poi_geometry, poi_properties)
    features.append(poi_feature)

testpt=ee.Geometry.Point([-112.0398,33.26879])

def pints(test2):
    for row in test2:
        features=[]
        print(dict(row))
        poi_geometry = ee.Geometry.Point([row[8],row[9]])
        print(poi_geometry)
        poi_properties = dict(row)
        poi_feature = ee.Feature(poi_geometry, poi_properties)
        features.append(poi_feature)
    return(features)

fest = pints(test2)

ee_fc = ee.FeatureCollection(features) 
ee_fc.getInfo()


def unique(test):
    uniquelist=list()
    for i in test:
        for j in i[1]:
        if 
        else:
            pass
    return(uniquelist)


#
fake = [['20-17', 12],['20-18', 12],['20-19', 12],['20-20', 12],['21-20', 56]]
def foo(fk):

    def subfoo(sb):
         print(sb)

    most_recent = int()
    prev_val = int()
    for sub in fk:        
        if sub[0].split('-')[0] != most_recent and sub[1] != prev_val:
            most_recent = sub[0].split('-')[0]
            prev_val = sub[1]
            subfoo(sub)
        else:
             pass
foo(fake)        
    





test2=unique(test)

print(test2[3:30])

                if line[0:1] not in uniquelist:
                    
                else:
                    pass