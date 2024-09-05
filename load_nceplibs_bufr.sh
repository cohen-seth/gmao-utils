#!/bin/bash

# ---------------------------
# $NCEPLIBS
# ---------------------------
set NCEPLIBS_latest_build = "/discover/nobackup/sicohen/workenv/NCEPLIBS-bufr/latest/build"
set NCEPLIBS = "$NCEPLIBS_latest_build/utils"
set PATH = "$NCEPLIBS_latest_build/bin:$PATH"
#set PYTHONPATH = "$NCEPLIBS_latest_build/lib64/python3.9/site-packages:$PYTHONPATH"
set PYTHONPATH = "$NCEPLIBS_latest_build/python"
set NCEPLIBS_py_tests = "$NCEPLIBS_latest_build/python/test"
set NCEPLIBS_py_utils = "$NCEPLIBS_latest_build/python/utils"

echo "NCEPLIBS_latest_build=" $NCEPLIBS_latest_build
echo "NCEPLIBS=" $NCEPLIBS

#alias sinv "$NCEPLIBS/sinv"

