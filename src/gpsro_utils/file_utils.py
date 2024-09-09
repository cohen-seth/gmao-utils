
import os
import sys
import subprocess
import pandas as pd
from pathlib import Path
import re
from discover_config import gmao_utils_dir,GPSRO_SPIRE_reanalysis,BufrTableC,wrkdir,outdir,iodadir

# source NOAA-PSL/observation-inventory-utils
def is_valid_readable_file(filepath):
    """
    Method to ensure that the filename/path is valid, exists, contains data,
    and the user has sufficient permissions to read it.
    """
    # look for invalid characters in filename/path
    try:
        m = re.search(r'[^A-Za-z0-9\._\-\/]', filepath)
        if m is not None and m.group(0) is not None:
            print(
                'Only a-z A-Z 0-9 and - . / _ characters allowed in filepath')
            raise ValueError(
                f'Invalid characters found in file path: {filepath}')
    except Exception as e:
        raise ValueError(f'Invalid file path: {e}')
    try:
        path = Path(filepath)
        if not path.is_file():
            raise ValueError(f'Path: {filepath} does not exist')
    except Exception as e:
        raise ValueError(f'Invalid file path: {e}')

    # check permissions on file
    status = os.stat(filepath, follow_symlinks=True)
    print(f'status.st_size: {status.st_size}')
    if status.st_size == 0:
        print(f'if block caught 0 byte file {status}')
        raise ValueError(f'Invalid file. File {filepath} is empty.')

    permissions = oct(status.st_mode)[-3:]
    readAccess = os.access(filepath, os.R_OK)
    if readAccess is False:
        raise ValueError(
            f'Insufficient permissions on file "{filepath}" - {permissions}.'
        )




# 1. generate a list of files within the given directory ----------------------------------------------------------------
    # path = '/discover/nobackup/sicohen/Data/gmao/bufr/AMSUA/Y2020/'
    # rootdir = sys.argv[1]
    # 'filelist' with be the list of bufr files that is returned (to then be used as input for the inventory tool)
    # loop over directory and all it's subdirectories, list whats in there but dont print everything, return only bufr files account for files name with extensions '.bufr' and '.bufr_d'


def get_file_list(rootdir):#,suffix):
    i = 0 
    filelist = []
    for subdir, dirs, files in os.walk(rootdir):
        print(f"{dirs}")
        print(f"----{subdir}")
        for idx, file in enumerate(files):
            if file.endswith(".bufr_d") or file.endswith(".nc4"):
                print (f"--------- {os.path.join(subdir, file)}")
                filepath = subdir + os.sep + file
                filelist.append(filepath)
                i+=1
                #if i == 32: break
    return(sorted(filelist))    #print(sorted(filelist))

# merge_bufr_code_table_c ~ merges satid names from NCEPLIBS-bufr Bufr Code Table C 
def merge_bufr_code_table_c(dataframe):
    # Merge the Bufr SAID codes ~ add names for satid's
    print(f' Now merging satid names from Bufr Code Table C')
    BufrCodes = pd.read_csv(BufrTableC)
    BufrCodes['SAID'] = BufrCodes['SAID'].astype(float).astype(int)
    BufrCodes['kx'] = BufrCodes['SAID'].abs().astype(int)
    dataframe['kx'] = dataframe['satid'].astype(int)
    dataframe = dataframe.merge(BufrCodes, how = 'outer', on = 'kx')
    dataframe = dataframe[~dataframe['bendingAngle'].isna()]
    return(dataframe)

