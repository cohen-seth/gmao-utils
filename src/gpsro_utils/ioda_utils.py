import sys 
from netCDF4 import Dataset
import pandas as pd
import subprocess
from discover_config import gmao_utils_dir,GPSRO_SPIRE_reanalysis,BufrTableC,wrkdir,outdir,iodadir
from file_utils import get_file_list,merge_bufr_code_table_c
from convert_ioda2df import nc_to_df
import numpy as np

#from ioda_utils import get_meta_data,get_obs_value,get_obs_error,satellite_id_subset,lat_window_subset,get_variable

# ---- (Helper) Functions

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

def satellite_id_subset(arr, kx):
    arr_kx = arr[np.isin(arr['satelliteIdentifier'], kx)]
    #print(arr.dtype.names)
    return(arr_kx)

def lat_window_subset(arr, window):
    arr_kx = arr[np.isin(arr['latitude'], window)]
    return(arr_kx)

def get_variable(data,group,name):
    x = data.groups[group].variables[name][:]
    return(x)
