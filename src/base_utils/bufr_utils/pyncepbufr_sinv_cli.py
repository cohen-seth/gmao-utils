# 2024-05-16 
# pyncepbufr_sinv_cli.py() ----------------------------------------------------------------
# (Previously referred to as sinv.py adn _10.27.2023.py)
import ncepbufr
import pandas as pd
import numpy as np
import sys 


#python pyncepbufr_sinv_cli.py [Data-Path] [-print] [-filter] [CLATH] [min latitude] [max latitude] 
#python pyncepbufr_sinv_cli.py $ObsBufr/test-mohar/gdas1_spnasa.211231.t18z.gpsro.tmO0.bufr_d -filter CLATH -30 30


# to change the amount of rows shown in output
#pd.set_option('display.max_rows', 1000))
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_colwidth',25)

def sinv(self, hdstr):
    bufr = ncepbufr.open(self)    #filename = str(file)
    bufr.checkpoint()
    x = []
    while bufr.advance() == 0:
        while bufr.load_subset() == 0:
            hdstr = hdstr
            hd = bufr.read_subset(hdstr).squeeze()
            x.append((hd))
    bufr.restore()
    x = pd.DataFrame(x)
    x.columns = hdstr.split() 
    x['filename'] = self.split("/")[-1]
    bufr.close()
    return x


#PathToBufrTableC = '/Users/sicohen/Work/GpsroTools/Data/bufr-code-table-C-sinv-merge.csv'
PathToBufrTableC = "/discover/nobackup/sicohen/Workshop/SicInventoryTools/dependencies/bufr-code-table-C-sinv-merge.csv" 

if len(sys.argv) > 1:
    if sys.argv[2] == '-print':
        input1 = sys.argv[1]
        input2 = 'SAID SIID YEAR MNTH DAYS HOUR MINU SECO CLATH CLONH filename'        
        y = sinv(input1, input2)
        # Bufr Code Table C (has definitions for SAID codes) www.emc.ncep.noaa.gov/mmb/data_processing/common_tbl_c1-c5.htm#c-5
        #PathToBufrTableC = '/Users/sicohen/Work/GpsroTools/Data/bufr-code-table-C-sinv-merge.csv'
        #PathToBufrTableC = "/discover/nobackup/sicohen/Workshop/SicInventoryTools/dependencies/bufr-code-table-C-sinv-merge.csv" 
        BufrTableC = pd.read_csv(PathToBufrTableC)
        BufrTableC['SAID'] = BufrTableC['SAID'].astype(float).astype(str)
        y['SAID'] = y['SAID'].astype(str)
        y = y.merge(BufrTableC, how = 'inner', on = 'SAID')
        total_subsets_by_said = y.groupby(['SAID', 'SIID', 'Code figure', 'filename']).size().to_frame('subsets')
        print()
        print("-----------------------------------------------------------------------------------")
        print(f"Table 1: `total_subsets_by_said` ----- Total Number of Subsets By SAID ~ `sinv` table (ALL INPUT FILES)")
        print(total_subsets_by_said)
        print()
        print("-----------------------------------------------------------------------------------")
    if sys.argv[2] == '-filter':
        var = sys.argv[3] 
        var_min = float(sys.argv[4])
        var_max = float(sys.argv[5])
        input1 = sys.argv[1]
        input2 = 'SAID SIID YEAR MNTH DAYS HOUR MINU SECO CLATH CLONH filename'
        y = sinv(input1, input2)
        y = y[(y[var] >= var_min) & (y[var] <= var_max)].sort_values(var)
        # Bufr Code Table C (has definitions for SAID codes) www.emc.ncep.noaa.gov/mmb/data_processing/common_tbl_c1-c5.htm#c-5
        #PathToBufrTableC = "/discover/nobackup/sicohen/Workshop/SicInventoryTools/dependencies/bufr-code-table-C-sinv-merge.csv"
        BufrTableC = pd.read_csv(PathToBufrTableC)
        BufrTableC['SAID'] = BufrTableC['SAID'].astype(float).astype(str)
        y['SAID'] = y['SAID'].astype(str)
        y = y.merge(BufrTableC, how = 'inner', on = 'SAID')
        print()
        print("-----------------------------------------------------------------------------------")
        print(f"Table 2: `tbl` ----- Subsets By SAID ~ Applied filter: {var_min} <= {var} <= {var_max}")
        print()
        #filtered_subset = tbl[(tbl[var] >= var_min) & (tbl[var] <= var_max)].sort_values(var)
        tbl = y.groupby(['SAID', 'SIID', 'Code figure', 'filename']).size().to_frame('subsets')
        print(tbl)
        print()
        print("-----------------------------------------------------------------------------------")
        print(f"Table 3: `y` ----- Dataframe ~ Applied filter: {var_min} <= {var} <= {var_max}")
        #print(y[['SAID', 'SIID', 'CLATH', 'CLONH']]) #, 'Code figure', 'filename']])
        print(y)
        print("-----------------------------------------------------------------------------------")




