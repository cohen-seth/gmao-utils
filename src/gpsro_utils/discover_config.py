# 2024-09-04
# python version of whats in .env
# config_handlers/discover_config.py


# 2: Environment Requirements
# ------------------------
# Create env variables and directories that gmao_utils uses
# ------------------------
# directory where gmao_utils is installed
gmao_utils_dir = "/discover/nobackup/sicohen/workenv/gmao-utils" # need to rerun this line from before b/c LoadJedi includes a purge.
#gmao_utils_src = "$gmao_utils_dir/src"

# directory with bufr files
GPSRO_SPIRE_reanalysis = "/discover/nobackup/projects/gmao/geos-it/mchattop/GPSRO_SPIRE_reanalysis/GPSRO_final"

# bufr code defenitions table
BufrTableC = gmao_utils_dir+"/src/config_handlers/bufr-code-table-C-sinv-merge.csv"

TestFileBufr = "/discover/nobackup/projects/gmao/input/dao_ops/obs/flk/ncep_g5obs/bufr/GPSRO/Y2020/M02/gdas1.200202.t00z.gpsro.tm00.bufr_d"

## 1.0: working directory path
#mkdir -p wrkdir/function-outputs/iodadir
wrkdir = gmao_utils_dir+"/wrkdir"
outdir = wrkdir+"/function-outputs" ## output directory
iodadir = outdir+"/iodadir"

