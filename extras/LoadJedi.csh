#!/usr/local/bin/csh

# Modules for ioda-converters
# ---------------------------

setenv jedibuild /discover/nobackup/sicohen/JediWork/latest/build-intel-release
setenv jedisrc /discover/nobackup/sicohen/JediWork/latest

module purge
source $jedibuild/modules
#module load jedi_bundle

# Ioda Python
setenv LD_LIBRARY_PATH $jedibuild/lib:$LD_LIBRARY_PATH
setenv PATH $jedibuild/bin:$PATH

#what worked for us
setenv PYTHONPATH $jedibuild/lib/python3.10/:$PYTHONPATH
setenv PYTHONPATH $jedibuild/lib/python3.10/pyioda:$PYTHONPATH
setenv PYTHONPATH $jedibuild/lib/python3.10/pyiodaconv:$PYTHONPATH
setenv PYTHONPATH $jedibuild/lib/python3.10/pyiodautils:$PYTHONPATH

#instructions on the ioda-conv webpage (not working)
#export PYTHONPATH=$jedibuild/lib/pyiodaconv:$PYTHONPATH
#export PYTHONPATH=$jedisrc/iodaconv/src:$PYTHONPATH
setenv IODATEST $jedibuild/iodaconv/test


# List modules
ml

# Convert
#python $jedibuild/bin/proc_gsi_ncdiag.py -o gsi/ ioda
