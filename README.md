# gmao-utils
NASA/GMAO. Tools for working with  data files in both BUFR and IODA (JEDI) format.

# Directory Structure (skeleton)

# Installation and Environment Setup

1. Clone the gmao-utils repo.
```sh
$ git clone https://github.com/cohen-seth/gmao-utils.git
```

2. Next, open and edit config_gmao_utils.sh *ONLY!* :
```sh
$ vim config_gmao_utils.sh
```

3. Change the variable '$gmao_utils_dir' (line 8) in the config_gmao_utils.sh file. Change it to the path where you have cloned gmao-utils.

4. *OPTIONAL* Then, you may want to inspect and verify LoadJedi.sh. You should NOT need to edit this file; HOWEVER, you may need to in the future if there is a more recent build of JEDI/IODA. The everything in this file must point to a current build of the JEDI IODA CONVERTERS.

5. Run the configuration:
```sh
$ source config_gmao_utils.sh
```
6. Verify that wrkdir/function-outputs/iodadir exists.

7. Run the following examples. 

# Function examples

1. convert_bufr2ioda.py
command structure: 
```sh
$ python src/gpsro_utils/convert_bufr2ioda.py [PATH TO BUFR FILE(S)]
```
The PATH you give can EITHER be a path to a directory containing BUFR files with NO TRAILING '/' --OR-- the full path to a singular BUFR file you wish to convert.

```sh
$ python src/gpsro_utils/convert_bufr2ioda.py /discover/nobackup/projects/gmao/geos-it/mchattop/GPSRO_SPIRE_reanalysis/GPSRO_final/Y2022/M01
```

2. convert_ioda2df.py
```sh
$ python src/gpsro_utils/convert_ioda2df.py [PATH OF IODA FILE(S)]
```

3. plot latitude counts by 5 degree bins
```sh
$ python src/gpsro_utils/plot_latitude_bins.py wrkdir/function-outputs/iodadir/GPSRO_final/Y2022/M01/gdas1_spnasa.220101.t00z.gpsro.tm00.ioda.nc4
```

4. plot latitude counts by 5 degree bins by kx (~kx groups)
```sh
$ python src/gpsro_utils/plot_latitude_bins_kx.py wrkdir/function-outputs/iodadir/GPSRO_final/Y2022/M01/gdas1_spnasa.220101.t00z.gpsro.tm00.ioda.nc4
```

5. nceplibs_sinv.py
```sh
$ python src/bufr_utils/nceplibs_sinv.py /discover/nobackup/projects/gmao/input/dao_ops/obs/flk/ncep_g5obs/bufr/GPSRO/Y2020/M02/gdas1.200202.t00z.gpsro.tm00.bufr_d
```
