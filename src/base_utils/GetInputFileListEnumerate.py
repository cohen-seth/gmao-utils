# 10/24/2023
# GetInputFileListEnumerate() ----------------------------------------------------------------
import os
import sys
    # path = '/discover/nobackup/sicohen/Data/gmao/bufr/AMSUA/Y2020/'
    # rootdir = sys.argv[1]
    # 'filelist' with be the list of bufr files that is returned (to then be used as input for the inventory tool)
    # loop over directory and all it's subdirectories, list whats in there but dont print everything, return only bufr files account for files name with extensions '.bufr' and '.bufr_d'
def GetInputFileListEnumerate(rootdir):#,suffix):
    filelist = []
    for subdir, dirs, files in os.walk(rootdir):
        print(f"{dirs}")
        print(f"----{subdir}")
        for idx, file in enumerate(files):
            if file.endswith("ioda.nc4"): # or file.endswith(".bufr_d"):
                print (f"--------- {os.path.join(subdir, file)}")
                filepath = subdir + os.sep + file
                filelist.append(filepath)
    return(sorted(filelist))    #print(sorted(filelist))

