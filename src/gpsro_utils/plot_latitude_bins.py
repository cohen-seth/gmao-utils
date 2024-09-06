# Plot ~ Latitude Counts (5 degree bins)
import matplotlib.pyplot as plt
import numpy as np
import sys
import subprocess
from netCDF4 import Dataset
from ioda_utils import get_meta_data,get_obs_value,get_obs_error,satellite_id_subset,lat_window_subset,get_variable

# data
#testfile = Dataset('wrkdir/function-outputs/iodadir/GPSRO_final/Y2022/M01/gdas1_spnasa.220101.t00z.gpsro.tm00.ioda.nc4', mode ='r')
ioda = Dataset(sys.argv[1], mode ='r')
latitude = get_variable(ioda,'MetaData','latitude')

#  plot data ----- 
plt.hist(latitude,bins=len(np.arange(-90,90,5.)))

# graph options
plt.xlabel('Latitude Bins (5 degrees)')
plt.ylabel('Counts')
plt.title('Latitude Counts (5 degree bins)',
          fontweight = "bold")

subprocess.run(['mkdir', '-p', 'wrkdir/figures'])
filepath = sys.argv[1]
filename = filepath.split("/")[-1]
fileparts = filename.split(".")
figure_path = "wrkdir/figures/latitude_counts_" + ("_").join(fileparts[0:3]) + ".png" 
plt.savefig(figure_path)

plt.show() 
