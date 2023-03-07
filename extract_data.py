#########Extraction Script##############
#####Author: Ashley Cale###########
###Date: 3.6.2023####

###This is the google earth engine api script that:
##1) creates earth engine feature class from extracted points 
##2) grabs the correct National Landcover Database earth engine asset 
##3) extracts variables from database
##4) generates url link to download data (this will look like original data with landcover column added)



####create ee feature class using object generated from read_files script#####
features=[]
for index,row in df2019.iterrows():
    print(dict(row))
    poi_geometry = ee.Geometry.Point([float(row['day_lon']),float(row['day_lat'])])
    print(poi_geometry)
    poi_properties = dict(row)
    poi_feature = ee.Feature(poi_geometry, poi_properties)
    features.append(poi_feature)

####feature class#####
ee_fc = ee.FeatureCollection(features) 
#ee_fc.getInfo()

####function for extracting point data from image####
def rasterExtraction(image):
    feature = image.sampleRegions(
        collection = ee_fc, # feature collection here
        scale = 30 # Cell size of raster
    )
    return feature

####assign and process earth engine asset#####
##Be sure to change the date to the most recent previous year distribution#####
###Available years:
#2001
#2004
#2006
#2008
#2011
#2013
#2016
#2019



NLCD_data = ee.ImageCollection('USGS/NLCD_RELEASES/2019_REL/NLCD')
#print('Products:', NLCD_data.aggregate_array('system:index'))
nlcd2019 = NLCD_data.filter(ee.Filter.eq('system:index', '2019')).first()
#print('Bands:', nlcd2000.bandNames())
landcover = nlcd2019.select('landcover')

testextract = rasterExtraction(landcover)


##assign url to object###
##follow url to download csv###
url_csv = testextract.getDownloadURL('csv')
url_csv