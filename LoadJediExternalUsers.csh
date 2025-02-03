#!/usr/local/bin/csh

#------------------------
# Load Swell/JEDI module
#------------------------
module purge
module load git git-lfs

# 3/7/2024 ~ Modules moved here
# shared location ~ module use /discover/nobackup/projects/gmao/advda/swell/jedi_modules
#source /discover/nobackup/projects/gmao/advda/swell/jedi_modules/modules-intel

source /discover/nobackup/projects/gmao/advda/swell/jedi_modules/modules-intel-sles15
#module use /discover/nobackup/sicohen/opt/modulefiles/core
#module load swell/Swell_sles15

#------------------------
# For External Users (i.e. anyone who isn't sicohen)
#------------------------
# SICOHEN ~ seth's discover nobackup directory

# Point to existing JEDI build
setenv SICOHEN /discover/nobackup/sicohen
setenv jedibuild $SICOHEN/JediWork/JEDI-FV3-1.1.0/build-intel-release
setenv jedisrc $SICOHEN/JediWork/JEDI-FV3-1.1.0
setenv PATH $jedibuild/bin:$PATH

# Enabling IODA converters
setenv LD_LIBRARY_PATH $jedibuild/lib:$LD_LIBRARY_PATH
setenv PYTHONPATH $jedibuild/lib/python3.9/:$PYTHONPATH
setenv PYTHONPATH $jedibuild/lib/python3.9/pyioda:$PYTHONPATH
setenv PYTHONPATH $jedibuild/lib/python3.9/pyiodaconv:$PYTHONPATH
setenv PYTHONPATH $jedibuild/iodaconv/src:$PYTHONPATH

# echo the loaded modules list
ml
pip list

# Print the environemnt variables used for paths to sicohen's build/directory
#echo printenv | grep "export"

echo "\n ---- Added Envirnoment Variables: ---- \n"
echo "SICOHEN=$SICOHEN"
echo "jedibuild=$jedibuild"
echo "jedisrc=$jedisrc"
