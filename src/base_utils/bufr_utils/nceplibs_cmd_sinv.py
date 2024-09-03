# 2024-05-16
# nceplibs_cmd_sinv.py
# Seth Cohen (GMAO/SSAI)

# Format of the output from NCEPLIBS-bufr sinv util

import subprocess
import config.discover_config #import gpsro_tools_dependencies
from config.obs_inv_utils_nceplibs_cmd_sinv import validate_args,get_sat_id,get_sat_id_name,get_obs_count,get_sat_inst_id,get_sat_inst_dsc,get_line_type 


#observation-inventory-utils/src/obs_inv_utils/nceplibs_cmd_sinv.py
#from nceplibs_cmds_sinv import *
SPACE_SEPARATOR_LEN = 2
SAT_ID_START = 0
SAT_ID_END = SAT_ID_START + 3
SAT_ID_NAME_START = SAT_ID_END + SPACE_SEPARATOR_LEN
SAT_ID_NAME_END = SAT_ID_NAME_START + 16
OBS_COUNT_START = SAT_ID_NAME_END + SPACE_SEPARATOR_LEN
OBS_COUNT_END = OBS_COUNT_START + 10
SAT_INST_ID_START = OBS_COUNT_END + SPACE_SEPARATOR_LEN
SAT_INST_ID_END = SAT_INST_ID_START + 3
SAT_INST_DSC_START = SAT_INST_ID_END + SPACE_SEPARATOR_LEN
SAT_INST_DSC_END = SAT_INST_DSC_START + 80

OBS_DATA_LINE = 'obs_data_line'
OBS_COUNT_TOTAL_LINE = 'obs_count_total_line'
FILLER_LINE = 'filler_line'

# INPUT
#TestDataFile = "/discover/nobackup/sicohen/Data/testing/gpsro/gdas1_spnasa.220101.t00z.gpsro.tm00.bufr_d"
bufr_file = gpsro_tools_dependencies.TestBufrFile

# Call and Run the NCEPLIBS-bufr sinv util
output = subprocess.run(
    ['sinv', bufr_file],
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
)
print(output.stdout)
print(output.stderr)

