# gmao-utils
NASA/GMAO. Tools for working with  data files in both BUFR and IODA (JEDI) format.

# Directory Structure (skeleton)
packaging_tutorial/
└── src/
    └── base_utils/
        └── bufr_utils/
                ├── __init__.py
                ├── sinv.py
                ├── binv.py
                ├── cmpbqm.py
                ...
        └── ioda_utils/
                ├── __init__.py
                ├── converter_bufr2ioda.py  #  ( put converters here?)
                ...
    └── gpsro_utils/
        ├── __init__.py
        ├── converter_bufr2ioda.py          # ( or put converters here?)
        ├── gpsro.py          
            ├── kx.py
            ├── lat_lon_window.py
            ...

