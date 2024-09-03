# 2024/03/28
# convert a directory of GPSRO bufr files to ioda using: gnssro_bufr2ioda


#
#gnssro_bufr2ioda 2021121200 /discover/nobackup/sicohen/Data/gmao/bufr/GPSRO/Y2021/M12/gdas1.211212.t00z.gpsro.tm00.bufr_d gpsro_ioda.nc4


from GetInputFileListEnumerate import *
import subprocess
import sys
import pandas as pd

# 5, 6, 
#rootdir= "/discover/nobackup/sicohen/Data/gmao/bufr/GPSRO/Y2009/M04"
rootdir=sys.argv[1]
#print(("/").join(rootdir.split("/")[-3:]))
####################################
#def convert_bufr_to_ioda(rootdir):
####################################
files = GetInputFileListEnumerate(rootdir)

y=[]
files_ioda=[]
i = 1
for file in files:
    print(f'Converting file {i} out of {len(files)}')
    filename = file.split("/")[-1]
    parts = filename.split(".")
    dates = "20" + parts[1]
    #parts = (".").join(parts)
    parts[-1] = "ioda.nc4"
    ioda_path = "/discover/nobackup/sicohen/Data/gmao/ioda/" + ("/").join(rootdir.split("/")[-3:])
    print(ioda_path)
    ioda_filename = ioda_path + "/" + (".").join(parts)
    x = ["gnssro_bufr2ioda", dates, file, ioda_filename]
    files_ioda.append((ioda_filename))
    print(x)
    subprocess.run(['mkdir','-p',ioda_path])
    subprocess.run(x)
    print(f' Progress: {round(i/len(files)*100)}%')
    y.append((x))
    
    
    
##
saved_list_path = ioda_path + "/files_ioda.csv"
#files_ioda = pd.DataFrame(files_ioda)
files_ioda.to_csv(saved_list_path, index=False)
print(f'--- File list output saved to: saved_list_path')
#return y