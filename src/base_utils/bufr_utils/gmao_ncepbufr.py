# GMAO Python library for working with BUFR files
# This is an extension of py-ncepbufr from NCEPLIBS (NOAA)
# Seth Cohen
# Created: 03-01-2024
# Last Modified:

from __future__ import print_function
import ncepbufr
import pandas as pd
import numpy as np
import sys 

# LEVEL 0 ~ base for reading bufr files
def get_gpsro():
    print(' (!) ATTENTION >>> get_gpsro has 6 outputs: out_data1b,out_data2a,out_roseq2,out_bnda,out_msgs,out_saids ')
    subset_counter = 0
    output = []
    print(f'----bufr.msg_counter: {bufr.msg_counter}----------')
    while bufr.advance() == 0:
        print(bufr.msg_counter, bufr.msg_type, bufr.msg_date)
        while bufr.load_subset() == 0:
            subset_counter += 1
            print(f'--------subset_counter: {subset_counter}------')
            hdr = get_bufr_hdrstr()
            print(hdr)
            
            
       
    
# LEVEL 1 ~ message level
def get_bufr_hdrstr():
    output = []
    hdrstr = default_hdrstr = 'YEAR MNTH DAYS HOUR MINU SECO SAID SIID'
    #if not isinstance(hdrstr,default_hdrstr):
    if not type(hdrstr) == type(default_hdrstr) or len(default_hdrstr) < 5:
        hdrstr = default_hdrstr
        msg = 'hdrstr must be of type string with a length > 5. It is' \
              f' actually of type: {type(hdrstr)} with length of {len(hdrstr)} \n ' \
              f' Defaulting to hdrstr equal to {default_hdrstr}'
        #raise TypeError(msg)
    print(f'---- Extracting Header Message Variables: {default_hdrstr}----------')
    hdr = bufr.read_subset(hdrstr).squeeze()
    yyyymmddhh ='%04i%02i%02i%02i%02i' % tuple(hdr.filled()[0:5])
    satid = int(hdr.filled()[6])
    siid = ptid = int(hdr.filled()[7])
    output.append(
        np.array(
            [bufr.msg_counter, bufr.msg_type, bufr.msg_date, yyyymmddhh, satid, ptid]
        )
    )
    return output


# LEVEL 2 ~ subset level

############################
# Modified scripts from the original py-ncepbufr python/test/ scripts
def test_gps(bufr,nmessages):
    prompt_help = 'f(x):`test_gps(bufr,nmessages)` requires: \n ' \
             f' (!!!) Failed? nmessages MUST be greater or equal to 3 because messages 1 and 2 have no subsets (data), only header/meta info. \n ' \
             f' (1) [bufr] an open bufr file ~ use ncepbufr.open("path/to/bufr/file.bufr") \n ' \
             f' (2) [nmessages] ~ the number of message to print. Set to 999999 to print the entire bufr file (all messages) \n '
    print(prompt_help)
    if nmessages < 3:
        prompt_warning = ' \n !! ATTENTION !! ~ you have set nmessages equal to a value less than 3. The command is going to abort. See the help prompt \n'
        print(prompt_warning)
    hdrstr ='YEAR MNTH DAYS HOUR MINU PCCF SAID SIID QFRO PD00'
    while bufr.advance() == 0:
        print(bufr.msg_counter, bufr.msg_type, bufr.msg_date)
        while bufr.load_subset() == 0:
            hdr = bufr.read_subset(hdrstr).squeeze()
            yyyymmddhh ='%04i%02i%02i%02i%02i' % tuple(hdr[0:5])
            satid = int(hdr[7])
            ptid = int(hdr[8])
            nreps_this_ROSEQ2 = bufr.read_subset('{ROSEQ2}').squeeze()
            nreps_this_ROSEQ1 = len(nreps_this_ROSEQ2)
            data1b = bufr.read_subset('ROSEQ1',seq=True) # bending angle
            data2a = bufr.read_subset('ROSEQ3',seq=True) # refractivity
            levs_bend = data1b.shape[1]
            levs_ref = data2a.shape[1]
            if levs_ref != levs_bend:
                print('skip report due to bending angle/refractivity mismatch')
                continue
            print('bufr.msg_counter,sat id,platform transitter id, levels, yyyymmddhhmm =',\
            bufr.msg_counter,satid,ptid,levs_ref,yyyymmddhh)
            print('k, height, lat, lon, ref, bend:')
            for k in range(levs_ref):
                rlat = data1b[0,k]
                rlon = data1b[1,k]
                height = data2a[0,k]
                ref = data2a[1,k]
                for i in range(int(nreps_this_ROSEQ2[k])):
                    m = 6*(i+1)-3
                    freq = data1b[m,k]
                    bend = data1b[m+2,k]
                    # look for zero frequency bending angle ob
                    if int(freq) == 0: break
                print(bufr.msg_counter,k,rlat,rlon,height,ref,bend)
        # only loop over first 6 subsets   \   if bufr.msg_counter == nmessages: break
        # for checking existence in locals() function
        #if 'nmessages' in locals() and type:
        if isinstance(nmessages, int):  # it is an integer
            # only loop over first 6 subsets
            if bufr.msg_counter == nmessages: break
            #return True
    #bufr.close()
    bufr.rewind()
    print(f'----------------------------------------------------------')
    exit_message = f'--  bufr has been rewound with bufr.rewind() to msg_count = {bufr.msg_counter}  -- ' 
    print(exit_message)
    print(f'----------------------------------------------------------')
 
############################
# Non-essential functions
# ~ i.e. fx's for personal preferences and testing

# Neater printing
def print_view(xstr,x):
    # print the name as a string, then print the 
    print(f'-------------------- {xstr} ------------------')
    print(x)
    print()

# Embedded mnemonic table in gpsro bufr file (may be subject to change)
# gettab gdas1_spnasa.220101.t00z.gpsro.tm00.bufr_d 
#|------------------------------------------------------------------------------|
#| ROSEQ1   | LTLONH  BEARAZ  {ROSEQ2}  PCCF                                    |
#|          |                                                                   |
#| ROSEQ2   | MEFR  IMPP  BNDA  FOST  201125  BNDA  201000  FOST                |
#|          |                                                                   |
#| ROSEQ3   | HEIT  ARFR  FOST  201123  ARFR  201000  FOST  PCCF                |
#|          |                                                                   |
#| ROSEQ4   | GPHTST  PRES  TMDBST  SPFH  FOST  201120  PRES  201000  201122    |
#| ROSEQ4   | TMDBST  201000  201123  SPFH  201000  FOST  PCCF                  |
#|          |                                                                   |
#|------------------------------------------------------------------------------|

