#!/usr/local/bin/zsh

# Modules for ioda-converters
# ---------------------------

export jedibuild = "/discover/nobackup/sicohen/JediWork/latest/build-intel-release"
export jedisrc = "/discover/nobackup/sicohen/JediWork/latest"

module purge
source $jedibuild/modules
#module load jedi_bundle

# Ioda Python
export LD_LIBRARY_PATH = "$jedibuild/lib:$LD_LIBRARY_PATH"
export PATH = "$jedibuild/bin:$PATH"

#what worked for us
export PYTHONPATH = "$jedibuild/lib/python3.10/:$PYTHONPATH"
export PYTHONPATH = "$jedibuild/lib/python3.10/pyioda:$PYTHONPATH"
export PYTHONPATH = "$jedibuild/lib/python3.10/pyiodaconv:$PYTHONPATH"
export PYTHONPATH = "$jedibuild/lib/python3.10/pyiodautils:$PYTHONPATH"

#instructions on the ioda-conv webpage (not working)
#export PYTHONPATH=$jedibuild/lib/pyiodaconv:$PYTHONPATH
#export PYTHONPATH=$jedisrc/iodaconv/src:$PYTHONPATH
export IODATEST = "$jedibuild/iodaconv/test"


# List modules
ml

# Convert
#python $jedibuild/bin/proc_gsi_ncdiag.py -o gsi/ ioda
