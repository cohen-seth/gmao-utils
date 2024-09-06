# gmao-utils
NASA/GMAO. Tools for working with  data files in both BUFR and IODA (JEDI) format.

# Directory Structure (skeleton)

# Step 1: Setting up your environment
git clone https://github.com/cohen-seth/gmao-utils.git

Next, you must change the variable 'gmao_utils_dir' in the config_gmao_utils.sh file. Change it to the path where you have cloned gmao-utils.

Then, inspect and verify LoadJedi.sh. You should NOT need to edit this file. It should point to a current build of the JEDI IODA CONVERTERS.
 

# Function examples

## convert_bufr2ioda.py
command structure: python src/gpsro_utils/convert_bufr2ioda.py [PATH TO BUFR FILE(S)]
The PATH you give can EITHER be a path to a directory containing BUFR files with NO TRAILING '/' --OR-- the full path to a singular BUFR file you wish to convert.

## Example python src/gpsro_utils/convert_bufr2ioda.py /discover/nobackup/projects/gmao/geos-it/mchattop/GPSRO_SPIRE_reanalysis/GPSRO_final/Y2022/M01


## convert_ioda2df.py
python src/gpsro_utils/convert_ioda2df.py [PATH OF IODA FILE(S)]

## plot latitude counts by 5 degree bins
python src/gpsro_utils/plot_latitude_bins.py wrkdir/function-outputs/iodadir/GPSRO_final/Y2022/M01/gdas1_spnasa.220101.t00z.gpsro.tm00.ioda.nc4

## plot latitude counts by 5 degree bins by kx (~kx groups)
python src/gpsro_utils/plot_latitude_bins_kx.py wrkdir/function-outputs/iodadir/GPSRO_final/Y2022/M01/gdas1_spnasa.220101.t00z.gpsro.tm00.ioda.nc4
