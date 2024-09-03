# 2024-09-03
# Seth Cohen (GMAO/SSAI)
# gmao_utils.bufr_utils.nceplibs_sinv.py
# NCEPLIBS-bufr utility sinv adaptation


import subprocess
import sys

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


# Call and Run the NCEPLIBS-bufr sinv util
bufr_file = sys.argv[1]
output = subprocess.run(
    ['sinv', bufr_file],
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
)
print(output.stdout)
