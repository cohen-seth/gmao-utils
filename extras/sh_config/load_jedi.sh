#!/bin/bash

# Modules for ioda-converters
# ---------------------------

set jedibuild = "/discover/nobackup/sicohen/JediWork/latest/build-intel-release"
set jedisrc = "/discover/nobackup/sicohen/JediWork/latest"

module purge
#source $jedibuild/modules
source $gmao_utils_dir/jedi_modules
#module load jedi_bundle

# Ioda Python
set LD_LIBRARY_PATH = "$jedibuild/lib:$LD_LIBRARY_PATH"
set PATH = "$jedibuild/bin:$PATH"

#what worked for us
set PYTHONPATH = "$jedibuild/lib/python3.10/:$PYTHONPATH"
set PYTHONPATH = "$jedibuild/lib/python3.10/pyioda:$PYTHONPATH"
set PYTHONPATH = "$jedibuild/lib/python3.10/pyiodaconv:$PYTHONPATH"
set PYTHONPATH = "$jedibuild/lib/python3.10/pyiodautils:$PYTHONPATH"

#instructions on the ioda-conv webpage (not working)
#export PYTHONPATH=$jedibuild/lib/pyiodaconv:$PYTHONPATH"
#export PYTHONPATH=$jedisrc/iodaconv/src:$PYTHONPATH"
set IODATEST = "$jedibuild/iodaconv/test"


# List modules
ml

# Convert
#python $jedibuild/bin/proc_gsi_ncdiag.py -o gsi/ ioda
