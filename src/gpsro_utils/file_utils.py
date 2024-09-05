
import os
import sys
import subprocess
from config_handlers.discover_config import gmao_utils_dir,GPSRO_SPIRE_reanalysis,BufrTableC,wrkdir,outdir,iodadir

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


