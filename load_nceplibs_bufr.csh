#/bin/csh

# ---------------------------
# $NCEPLIBS
# ---------------------------
#setenv NCEPLIBS_latest_build = "/discover/nobackup/sicohen/workenv/NCEPLIBS-bufr/latest/build"

setenv PATH /discover/nobackup/sicohen/workenv/NCEPLIBS-bufr/NCEPLIBS-bufr-bufr_v12.0.0/build/utils:$PATH
setenv NCEPLIBSbuild $NOBACKUP/workenv/NCEPLIBS-bufr/NCEPLIBS-bufr-bufr_v12.0.0/build
setenv NCEPLIBS $NCEPLIBSbuild/utils
setenv PATH $NCEPLIBSbuild/bin:$PATH
setenv PYTHONPATH $NCEPLIBSbuild/lib64/python3.9/site-packages:$PYTHONPATH
setenv NCEPLIBS_py_tests $NOBACKUP/workenv/NCEPLIBS-bufr/NCEPLIBS-bufr-bufr_v12.0.0/python/test
setenv NCEPLIBS_py_utils $NOBACKUP/workenv/NCEPLIBS-bufr/NCEPLIBS-bufr-bufr_v12.0.0/python/utils

#echo "NCEPLIBS_latest_build=" $NCEPLIBS_latest_build
echo "NCEPLIBSbuild=" $NCEPLIBSbuild
echo "NCEPLIBS=" $NCEPLIBS

#alias sinv "$NCEPLIBS/sinv"

