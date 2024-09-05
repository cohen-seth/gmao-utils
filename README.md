# gmao-utils
NASA/GMAO. Tools for working with  data files in both BUFR and IODA (JEDI) format.

# Directory Structure (skeleton)

# Step 1: Setting up your environment
git clone https://github.com/cohen-seth/gmao-utils.git

Next, you must change the variable 'gmao_utils_dir' in the config_gmao_utils.sh file. Change it to the path where you have cloned gmao-utils.

Then, inspect and verify LoadJedi.sh. You should NOT need to edit this file. It should point to a current build of the JEDI IODA CONVERTERS.
 

# Function examples

## convert_bufr2ioda.py
command structure: python src/gpsro_utils/convert_bufr2ioda.py [PATH]
The PATH you give can EITHER be a path to a directory containing BUFR files with NO TRAILING '/' --OR-- the full path to a singular BUFR file you wish to convert.

## Example python src/gpsro_utils/convert_bufr2ioda.py /discover/nobackup/projects/gmao/geos-it/mchattop/GPSRO_SPIRE_reanalysis/GPSRO_final/Y2022/M01
