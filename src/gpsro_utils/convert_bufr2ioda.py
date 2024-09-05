# 2024-09-04
# convert a directory of GPSRO bufr files to ioda using: gnssro_bufr2ioda


# example cli setup ~ gnssro_bufr2ioda 2021121200 /discover/nobackup/sicohen/Data/gmao/bufr/GPSRO/Y2021/M12/gdas1.211212.t00z.gpsro.tm00.bufr_d gpsro_ioda.nc4


#from GetInputFileListEnumerate import *
import os
import sys
import pandas as pd
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

# user input in cli (a path to where the files you want to convert are in) ~  '/discover/nobackup/sicohen/Data/gmao/bufr/AMSUA/Y2020/M01'
rootdir=sys.argv[1]
#rootdir = "/discover/nobackup/projects/gmao/geos-it/mchattop/GPSRO_SPIRE_reanalysis/GPSRO_final/Y2022/M01"
# list of files 
files = get_file_list(rootdir)
print(f'files: \n {files}')

y=[]
#files_ioda=[]
i = 1
for file in files:
    print(f'Converting file {i} out of {len(files)}')
    filename = file.split("/")[-1]
    parts = filename.split(".")
    dates = "20" + parts[1]
    #parts = (".").join(parts)
    parts[-1] = "ioda.nc4"
    ioda_subdir = iodadir + ("/").join(rootdir.split("/")[-3:])
    print(ioda_subdir)
    ioda_filename = iodadir + "/" + (".").join(parts)
    x = ["gnssro_bufr2ioda", dates, file, ioda_filename]
    #files_ioda.append((ioda_filename))
    print(x)
    subprocess.run(['mkdir','-p',ioda_subdir])
    subprocess.run(x)
    print(f' Progress: {round(i/len(files)*100)}%')
    i+=1 #y.append((x))
    
    
    
##
#saved_list_path = iodadir + "/files_ioda.csv"
#files_ioda = pd.DataFrame(files_ioda)
#files_ioda.to_csv(saved_list_path, index=False)
#print(f'--- File list output saved to: saved_list_path')
print(f'--- Bufr files converted to ioda and saved to {ioda_subdir}')
#return y
