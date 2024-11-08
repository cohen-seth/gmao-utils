import subprocess


# Basic sinv to be used in the command line
def sinv_base(bufr):
    # User input: path to bufr file  --  bufr_file = sys.argv[1]
    # Call and Run the NCEPLIBS-bufr sinv util
    output = subprocess.run(
        ['sinv', bufr],
        capture_output = True, # Python >= 3.7 only
        text = True # Python >= 3.7 only
    )
    #print(f' --- sinv output for: {bufr_file}')
    print(output.stdout)
    return(output.stdout)



