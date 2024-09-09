#!/bin/bash

# 2024-09-04
# Seth Cohen (GMAO/SSAI)
# Environment Requirements

# ------------------------
# Load Jedi First ~ need ioda converters from IODACONV and PYIODA. 
# ------------------------
set gmao_utils_dir = "/discover/nobackup/sicohen/workenv/gmao-utils"
source $gmao_utils_dir/load_jedi.sh
source $gmao_utils_dir/load_nceplibs_bufr.sh

# ------------------------
# Create env variables and directories that gmao_utils uses
# ------------------------
# directory where gmao_utils is installed
set gmao_utils_dir = "/discover/nobackup/sicohen/workenv/gmao-utils" # need to rerun this line from before b/c LoadJedi includes a purge.
set gmao_utils_src = "$gmao_utils_dir/src"

# directory with bufr files
set GPSRO_SPIRE_reanalysis = "/discover/nobackup/projects/gmao/geos-it/mchattop/GPSRO_SPIRE_reanalysis/GPSRO_final"

# bufr code defenitions table
set BufrTableC = "$gmao_utils_src/config_handlers/bufr-code-table-C-sinv-merge.csv"


## 1.0: working directory path
mkdir -p wrkdir/function-outputs/iodadir
set wrkdir = "$gmao_utils_dir/wrkdir"
set outdir = "$wrkdir/function-outputs" ## output directory
set iodadir = "$outdir/iodadir" 

## 1.1: test input data
#TestBufrFile = "/discover/nobackup/sicohen/Data/testing/gpsro/gdas1_spnasa.220101.t00z.gpsro.tm00.bufr_d"
#TestIodaFile = "/discover/nobackup/sicohen/Data/testing/gpsro/gdas1_spnasa.220121.t18z.gpsro.tm00.ioda.nc4"

# show whats loaded
#ml ~ LoadJedi does this already
pip list
echo "\n"
echo " --- The following variables have been set to these respective paths: ------------------------------ \n"
echo "gmao_utils_dir="$gmao_utils_dir
echo "gmao_utils_src="$gmao_utils_src
echo "BufrTableC="$BufrTableC
echo "wrkdir="$wrkdir
echo "outdir="$outdir
echo "GPSRO_SPIRE_reanalysis="$GPSRO_SPIRE_reanalysis
echo "\n"
echo "--- NCEPLIBS ---"
echo "NCEPLIBS_latest_build=" $NCEPLIBS_latest_build
echo "NCEPLIBS=" $NCEPLIBS
echo "\n"

echo " You have successfully loaded gmao_utils python package. \n  --- HOWEVER ---, you should ensure that all paths are correct before proceeding.\n"
