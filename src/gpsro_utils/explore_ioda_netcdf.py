from netCDF4 import Dataset
import numpy as np
import pandas as pd

data = Dataset("gdas1_spnasa.220101.t00z.gpsro.tm00.ioda.nc4", mode='r')
#data = Dataset("Data/gdas1_spnasa.220101.t06z.gpsro.tm00.ioda.nc4", mode='r')
#data = Dataset("gdas1_spnasa.220101.t00z.gpsro.tm00.ioda.nc4", mode='r')
print(data)

def get_meta_data(data):
    MetaData = data.groups['MetaData']
    print(MetaData)
    return(MetaData)

def get_obs_value(data):
    ObsValue = data.groups['ObsValue']
    print(ObsValue)
    return(ObsValue)

def get_obs_error(data):
    ObsError = data.groups['ObsError']
    print(ObsError)
    return(ObsError)

    

MetaData = get_meta_data(data)
ObsValue = get_obs_value(data)
ObsError = get_obs_error(data)

#print(MetaData)
#print(ObsValue)
#print(ObsError)

print(f' \n --- 1 --- MetaData: ----- \n {MetaData}')
#print(f' \n --- 1 --- MetaData.variables: ----- \n {MetaData.variables}')


print(f' \n --- 2 --- ObsValue: ----- \n {ObsValue}')
#print(f' \n --- 2 --- ObsValue.variables: ----- \n {ObsValue.variables}')


print(f' \n --- 3 --- ObsError: ----- \n {ObsError}')
#print(f' \n --- 3 --- ObsError.variables: ----- \n {ObsError.variables}')

#ObsValue.variables
#ObsError.variables

# MetaData
dateTime = data.groups['MetaData'].variables['dateTime'][:]
longitude = data.groups['MetaData'].variables['longitude'][:]
latitude = data.groups['MetaData'].variables['latitude'][:]
sequenceNumber = data.groups['MetaData'].variables['sequenceNumber'][:]
satelliteConstellationRO = data.groups['MetaData'].variables['satelliteConstellationRO'][:]
satelliteTransmitterId = data.groups['MetaData'].variables['satelliteTransmitterId'][:]
satelliteIdentifier = data.groups['MetaData'].variables['satelliteIdentifier'][:]
occulting_sat_is = data.groups['MetaData'].variables['occulting_sat_is'][:]
satelliteAscendingFlag = data.groups['MetaData'].variables['satelliteAscendingFlag'][:]
#
height = data.groups['MetaData'].variables['height'][:]
adjustLocalSpectralWidth = data.groups['MetaData'].variables['adjustLocalSpectralWidth'][:]
impactParameterRO = data.groups['MetaData'].variables['impactParameterRO'][:]
impactHeightRO = data.groups['MetaData'].variables['impactHeightRO'][:]
sensorAzimuthAngle = data.groups['MetaData'].variables['sensorAzimuthAngle'][:]
geoidUndulation = data.groups['MetaData'].variables['geoidUndulation'][:]
earthRadiusCurvature = data.groups['MetaData'].variables['earthRadiusCurvature'][:]
# ObsValue
bendingAngle = data.groups['ObsValue'].variables['bendingAngle'][:]
# ObsError
atmosphericRefractivity = data.groups['ObsValue'].variables['atmosphericRefractivity'][:]

"""
dateTime,longitude,latitude,sequenceNumber,satelliteConstellationRO,satelliteTransmitterId,satelliteIdentifier,occulting_sat_is,satelliteAscendingFlag,height,adjustLocalSpectralWidth,
impactParameterRO,impactHeightRO,sensorAzimuthAngle,geoidUndulation,earthRadiusCurvature,atmosphericRefractivity,bendingAngle

dateTime,longitude,latitude,sequenceNumber,satelliteConstellationRO,satelliteTransmitterId,satelliteIdentifier,occulting_sat_is,satelliteAscendingFlag,height,adjustLocalSpectralWidth,
impactParameterRO,impactHeightRO,sensorAzimuthAngle,geoidUndulation,earthRadiusCurvature,atmosphericRefractivity,bendingAngle
"""
"""

#
dateTime = data.groups['MetaData'].variables['dateTime'][:]
dateTime_converted = pd.to_datetime(dateTime,unit='s') 

lon = data.groups['MetaData'].variables['longitude'][:]
lat = data.groups['MetaData'].variables['latitude'][:]
#
satid = data.groups['MetaData'].variables['satelliteIdentifier'][:]
satConstRO = data.groups['MetaData'].variables['satelliteConstellationRO'][:]
satTransId = data.groups['MetaData'].variables['satelliteTransmitterId'][:]

#
refr = data.groups['ObsValue'].variables['atmosphericRefractivity'][:]
bnda = data.groups['ObsValue'].variables['bendingAngle'][:]

#xy = np.rec.fromarrays([dateTime_converted,dateTime,lat, lon, bnda,satid])
#xy
"""

# ---- Create Working/Testing Data ~ Numpy array that will be used

#dateTime,longitude,latitude,sequenceNumber,satelliteConstellationRO,satelliteTransmitterId,satelliteIdentifier,occulting_sat_is,satelliteAscendingFlag,height,adjustLocalSpectralWidth,
#impactParameterRO,impactHeightRO,sensorAzimuthAngle,geoidUndulation,earthRadiusCurvature,atmosphericRefractivity,bendingAngle

dateTime_converted = pd.to_datetime(dateTime,unit='s') 
dtype = {'names' : ['dateTime_converted', 'dateTime', 'latitude', 'longitude', 'bendingAngle','satelliteIdentifier'],
         'formats' : ['datetime64[ns]','int64','float32','float32','float32','int32']}
arr = np.rec.fromarrays([dateTime_converted, dateTime, latitude, longitude, bendingAngle, satelliteIdentifier], dtype = dtype)
arr['latitude']
arr.dtype.names

# ---- (Helper) Functions
def satellite_id_subset(arr, kx):
    arr_kx = arr[np.isin(arr['satelliteIdentifier'], kx)]
    #print(arr.dtype.names)
    return(arr_kx)

def lat_window_subset(arr, window):
    arr_kx = arr[np.isin(arr['latitude'], window)]
    return(arr_kx)



unique, counts = np.unique(arr['satelliteIdentifier'], return_counts=True)
dict(zip(unique, counts))

cosmic2 = [750,751,752,753,754,755]
#cosmic2 = [740,741,742,743,744,745]
spire = [269]
metop = [4,5]
other = [42,43,44,786,800,803,804,820,825]

print(f'satellite_id_subset(arr, kx=cosmic2): \n  \n {arr.dtype.names} \n {satellite_id_subset(arr, kx=cosmic2)} \n \n')
print(f' ---- \n \n ')
print(f'satellite_id_subset(arr, kx=spire): \n \n {arr.dtype.names} \n {satellite_id_subset(arr, kx=spire)}')

#arr = satellite_id_subset(arr, kx=cosmic2)
#satellite_id_subset(arr, kx=metop)
#satellite_id_subset(arr, kx=other)

#lat_window_subset(arr, [-90.,90.])
#unique, counts = np.unique(arr_bucket['satelliteIdentifier'], return_counts=True)

#d = np.rec.fromarrays([dateTime_converted,dateTime,lat, lon, bnda, satid], dtype = dtype)
#dtype = {'names' : ['dateTime_converted', 'dateTime', 'latitude', 'longitude', 'bendingAngle','satid','bucket'],
#         'formats' : ['datetime64[ns]','int64','float32','float32','float32','int32','int32']}

deltalat = 5.
#bucket = []
table_kx = []
bucket = 0
print(f'bucket,(window),[satelliteIdentifier],[counts] \n')

for lat_lower in np.arange(-90,90,deltalat):
    bucket+=1
    lat_upper = lat_lower + deltalat
    window = (lat_lower,lat_upper)
    arr_bucket = arr[(arr['latitude'] >= lat_lower) & (arr['latitude'] < lat_upper)]       #& ((kx==740) | (kx==741) | (kx==742) | (kx==743) | (kx==744) | (kx==745)))
    unique, counts = np.unique(arr_bucket['satelliteIdentifier'], return_counts=True)
    table_counts = dict(zip(unique, counts))
    #table_counts = list(zip(unique, counts))
    #print(f'bucket,window,[satelliteIdentifier],[counts])')
    print(bucket,window,list(unique),list(counts))
    #print(bucket,window,list(table_counts))

    

# Plot 1 ~ Latitude Counts (5 degree bins)
import matplotlib.pyplot as plt
#  ----- 1
#plt.hist(arr['latitude'])

#  ----- 2
#len(np.arange(-90,90,deltalat))
len(np.arange(-90,90,5.))
plt.hist(arr['latitude'],bins=len(np.arange(-90,90,5.)))

plt.xlabel('Latitude')
plt.ylabel('Counts')
plt.xticks(np.arange(-90,90+10,10.))
plt.title('Test - Latitude Counts (5 degree bins)',
          fontweight = "bold")
#df.hist('N', by='Letter')
plt.savefig('Latitude_Counts_5_degree_bins_test.png')
plt.show() 



# Plot 3 ~ Geospatial Map 
#from matplotlib import colormaps
import netCDF4 as nc4
import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
import numpy.ma as ma
#import colormaps
from numpy import *
#import gmao_tools as gt
#import ncdiag as ncd
#import matplotlib.mlab as mlab
#import datetime
#from datetime import datetime, timedelta
#import matplotlib.dates as mdates
from netCDF4 import Dataset,num2date
from scipy.stats import gaussian_kde
import matplotlib.cm as cm
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
import cartopy.feature as cfeature

#cm = colormaps.colormaps()
#cmap = cm.newjet_centergray


fig = plt.figure(figsize=(11, 5), dpi=86, facecolor="w")
ax = fig.add_subplot(1,1,1, projection=ccrs.Robinson())

ax.set_global()

ax.add_feature(cfeature.COASTLINE, edgecolor="black")
ax.add_feature(cfeature.BORDERS, edgecolor="black")
ax.gridlines()

plt.scatter(x=arr['longitude'],y=arr['latitude'],color="dodgerblue",s=1,alpha=0.5,transform=ccrs.PlateCarree()) ## Important
plt.title('Test ~ Geospatial Map ', fontsize = 12) 
#leg=plt.legend(loc='best',markerscale=5)
#for lh in leg.legendHandles:
#    lh.set_alpha(1)

plt.tight_layout()
plt.savefig('Geospatial_distribution_test.png')
plt.show()
