# 2024-09-04
# convert a directory of GPSRO bufr files to ioda using: gnssro_bufr2ioda


# example cli setup ~ gnssro_bufr2ioda 2021121200 /discover/nobackup/sicohen/Data/gmao/bufr/GPSRO/Y2021/M12/gdas1.211212.t00z.gpsro.tm00.bufr_d gpsro_ioda.nc4


#from GetInputFileListEnumerate import *
import os
import sys
import pandas as pd
import subprocess
from pathlib import Path
import os.path
from discover_config import gmao_utils_dir,GPSRO_SPIRE_reanalysis,BufrTableC,wrkdir,outdir,iodadir
from file_utils import get_file_list, is_valid_readable_file


"""
# user input in cli (a path to where the files you want to convert are in) ~  '/discover/nobackup/sicohen/Data/gmao/bufr/AMSUA/Y2020/M01'
rootdir=sys.argv[1]
#rootdir = "/discover/nobackup/projects/gmao/geos-it/mchattop/GPSRO_SPIRE_reanalysis/GPSRO_final/Y2022/M01"
is_valid_readable_file(rootdir)
# list of files 
if(is_valid_readable_file(rootdir) == True):
    files = rootdir
    print(f'input is a single file. Converting input bufr file to ioda.nc4')
#elif(is_valid_readable_file(rootdir) == False):
else:
    files = get_file_list(rootdir)
    print(f'files: \n {files}')
from pathlib import Path
"""

#my_file = Path(rootdir)
rootdir=sys.argv[1]
input1 = Path(sys.argv[1])


if input1.is_file():
    # file exists
    files = [sys.argv[1]]
    ioda_subdir = iodadir + "/" + ("/").join(rootdir.split("/")[-4:-1])
    print(f'input is a file: \n {files}')
if input1.is_dir():
    # directory exists    
    files = get_file_list(sys.argv[1])
    ioda_subdir = iodadir + "/" + ("/").join(rootdir.split("/")[-3:])
    print(f'input is a directory: \n {files}')

# Create directory for output files if needed
print(f'ioda_subdir: {ioda_subdir}')
subprocess.run(['mkdir','-p',ioda_subdir])


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
    #ioda_subdir = iodadir + "/" + ("/").join(rootdir.split("/")[-3:])
    #subprocess.run(['mkdir','-p',ioda_subdir])
    ioda_filename = ioda_subdir + "/" + (".").join(parts)
    if (os.path.isfile(ioda_filename) == True):
        print(f'File already exists. Skipping.')
        continue
    elif (os.path.isfile(ioda_filename) == False):
        print(f'No file found. Converting.')
        x = ["gnssro_bufr2ioda", dates, file, ioda_filename]
        print(x)
        subprocess.run(x)
    print(f' Progress: {round(i/len(files)*100)}%')
    i+=1 
    print(f'--- Bufr files converted to ioda and saved to {ioda_subdir}') 
    #files_ioda.append((ioda_filename))    
    #y.append((x))
    
    
    
##
#saved_list_path = iodadir + "/files_ioda.csv"
#files_ioda = pd.DataFrame(files_ioda)
#files_ioda.to_csv(saved_list_path, index=False)
#print(f'--- File list output saved to: saved_list_path')
#print(f'--- Bufr files converted to ioda and saved to {ioda_subdir}')
#return y
