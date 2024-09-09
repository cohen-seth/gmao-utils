# subset by kx and plot latitude 5 degree bins
import pandas as pd
import sys
import numpy as np 
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import subprocess 

# gmao_utils
from discover_config import gmao_utils_dir,GPSRO_SPIRE_reanalysis,BufrTableC,wrkdir,outdir,iodadir
from ioda_utils import get_meta_data,get_obs_value,get_obs_error,satellite_id_subset,lat_window_subset,get_variable

#data = sys.argv[1]
data = Dataset(sys.argv[1], mode ='r')


# creating array from ioda netcdf4 data file
## def get_variable(data,group,name):
dateTime = pd.to_datetime(get_variable(data,'MetaData','dateTime'),unit='s') 
latitude = get_variable(data,'MetaData','latitude')
longitude = get_variable(data,'MetaData','longitude')
bendingAngle = get_variable(data,'ObsValue','bendingAngle')
satelliteIdentifier = get_variable(data,'MetaData','satelliteIdentifier')

dtype = {'names' : ['dateTime', 'latitude', 'longitude', 'bendingAngle','satelliteIdentifier'],
         'formats' : ['datetime64[ns]','float32','float32','float32','int32']}

arr = np.rec.fromarrays([dateTime, latitude, longitude, bendingAngle, satelliteIdentifier], dtype = dtype)

# kx definitions
cosmic2 = [750,751,752,753,754,755]
cosmic = [740,741,742,743,744,745]
spire = [269]
metop = [4,5]
other = [42,43,44,786,800,803,804,820,825]

# loop over kx groups and plot latitude counts by 5 degree bins
c=0
colors = ['blue','orange','green','red','purple','black','cyan','pink','brown']
for kx in [cosmic,cosmic2,spire,metop,other]:
    c += 1
    print(kx)
    dt = satellite_id_subset(arr, kx)
    plt.hist(dt['latitude'], bins=len(np.arange(-90,90,5.)), color = colors[c])
    plt.xticks(np.arange(-90,90+10,10.))
    plt.xlabel('Latitude')
    plt.ylabel('Counts')
    plt.title(f'Latitude Counts (5 degree bins)  \n kx: {kx}',
              fontweight = "bold")
    subprocess.run(['mkdir', '-p', 'wrkdir/figures'])
    plt.savefig(f'wrkdir/figures/Latitude_Counts_5_degree_bins_kx_test_{c}.png')
    print(f'Plot(s) saved to: wrkdir/figures/Latitude_Counts_5_degree_bins_kx_test_{c}.png')
