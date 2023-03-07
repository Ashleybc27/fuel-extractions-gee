##This reads in all .txt files in a folder##
##Deprectiated, do this one at a time to make sure the extracted years match##
def readin(path):
    files = os.listdir(path)
    #print(files)
    allpoints=list()
    for i in files:
        with open(i, 'r') as _i_:
            for line in _i_:
                line = line.strip('\n')
                line = line.split(',')
                allpoints.append(line)
            del(allpoints[0])
    return(allpoints)


os.chdir(path)            
path='/Users/ashley/Documents/GitHub/fuel_extractions_gee/smalltest'
test=readin(os.getcwd())
print(test[0])
len(test)

###Determine the unique fire ID's for each year###
##Depreciated, this work will be done by year so the year sorting isn't nessecary
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
print(test2[0])
len(test2)
test3= pd.DataFrame(test2, columns = ["date","fireID","fire_len","pm_sum_fire_ug","ba_sum_fire","pm_sum_day","ba_sum_day","heat_sum_day","day_lat","day_lon"])
len(test2)  