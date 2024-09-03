# Seth Cohen
# 2024-09-03
# gmao_utils
# gpsro_utils.ioda_tuils.py

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
