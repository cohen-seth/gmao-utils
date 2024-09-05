
import os
import sys
import subprocess
from discover_config import gmao_utils_dir,GPSRO_SPIRE_reanalysis,BufrTableC,wrkdir,outdir,iodadir


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
            if file.endswith(".bufr_d"):
                print (f"--------- {os.path.join(subdir, file)}")
                filepath = subdir + os.sep + file
                filelist.append(filepath)
                i+=1
                if i == 5: break
    return(sorted(filelist))    #print(sorted(filelist))

# merge_bufr_code_table_c ~ merges satid names from NCEPLIBS-bufr Bufr Code Table C 
def merge_bufr_code_table_c(dataframe):
    # Merge the Bufr SAID codes ~ add names for satid's
    BufrCodes = pd.read_csv('BufrTableC')
    BufrCodes['SAID'] = BufrCodes['SAID'].astype(float).astype(int)
    BufrCodes['kx'] = BufrCodes['SAID'].abs().astype(int)
    dataframe['kx'] = dataframe['satid'].astype(int)
    dataframe = dataframe.merge(BufrCodes, how = 'outer', on = 'kx')
    dataframe = dataframe[~dataframe['bendingAngle'].isna()]
    return(dataframe)

