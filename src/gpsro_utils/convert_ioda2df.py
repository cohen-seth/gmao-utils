import sys
from netCDF4 import Dataset
import pandas as pd
import subprocess
from discover_config import gmao_utils_dir,GPSRO_SPIRE_reanalysis,BufrTableC,wrkdir,outdir,iodadir
from file_utils import get_file_list,merge_bufr_code_table_c

#data = nc.Dataset("gdas1_spnasa.220101.t00z.gpsro.tm00.ioda.nc4", mode='r')
#files_ioda = ["gdas1_spnasa.220101.t00z.gpsro.tm00.ioda.nc4"]
#test_file = iodadir + "/" + "gdas1_spnasa.220101.t00z.gpsro.tm00.ioda.nc4"
#files_ioda = [test_file]
# user input in cli (a path to where the files you want to convert are in) ~  '/discover/nobackup/sicohen/Data/gmao/bufr/AMSUA/Y2020/M01'
rootdir=sys.argv[1]

# generate list of ioda files you want to convert
files_ioda = get_file_list(rootdir)

def nc_to_df(files_ioda):
    df_all = pd.DataFrame([], columns = ['dateTime', 'latitude', 'longitude', 'bendingAngle','impp',
                                    'satid','seq', 'satConstRO', 'satTransId','geoidU', 'refr',
                                    'filename','filepath'])
    j=0
    for i in files_ioda:
        j+=1
        print(f'Converting (.nc4 to pandas Dataframe) file {j} out of {len(files_ioda)}: {i}')
        data = Dataset(i, mode='r')
        df = pd.DataFrame(
            {
                'dateTime': data.groups['MetaData'].variables['dateTime'][:], 
                'latitude': data.groups['MetaData'].variables['latitude'][:],
                'longitude': data.groups['MetaData'].variables['longitude'][:],
                'bendingAngle': data.groups['ObsValue'].variables['bendingAngle'][:],
                'impp': data.groups['MetaData'].variables['impactParameterRO'][:],
                'satid': data.groups['MetaData'].variables['satelliteIdentifier'][:],
                'seq': data.groups['MetaData'].variables['sequenceNumber'][:],
                'satConstRO': data.groups['MetaData'].variables['satelliteConstellationRO'][:],
                'satTransId': data.groups['MetaData'].variables['satelliteTransmitterId'][:],
                'geoidU': data.groups['MetaData'].variables['geoidUndulation'][:],
                'refr': data.groups['ObsValue'].variables['atmosphericRefractivity'][:],
                'filename':i.split("/")[-1],
                'filepath':i,
                'filedate':i.split(".")[1],
                'filecycle':i.split(".")[2],
                'filedatetime':i.split(".")[1] + i.split(".")[2],
                'DATE': pd.to_datetime(data.groups['MetaData'].variables['dateTime'][:],unit='s') 
                        #pd.to_datetime(df['dateTime'],unit='s')
            }
        )
        #print(df)
        print(i)
        print(j)
        df = merge_bufr_code_table_c(df)
        ioda_subdir = iodadir + "/" + ("/").join(rootdir.split("/")[-3:])
        filename = ioda_subdir + "/" + i.split("/")[-1] + ".csv"
        print(filename)
        df.to_csv(filename)
        #df_all = pd.concat([df_all,df])
        print(f' Progress: {round(j/len(files_ioda)*100)}%')
    print(f' Now merging satid names from Bufr Code Table C...')
    # merge satid names from Bufr Code Table C
    df_all = merge_bufr_code_table_c(df_all)
    return(df_all)


#print(f' Now merging satid names from Bufr Code Table C')
# merge satid names from Bufr Code Table C
df = nc_to_df(files_ioda)
#df = merge_bufr_code_table_c(df)
#ioda_subdir = iodadir + ("/").join(rootdir.split("/")[-3:])
#filename = ioda_subdir + "/" + ("_").join(rootdir.split("/")[-3:]) + ".csv"
#print(filename)
print(f'{df}')
