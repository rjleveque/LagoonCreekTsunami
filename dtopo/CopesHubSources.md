(CopesHubSources)=
# Copes Hub Sources

All 36 KinOkada sources that are described on
the page [Cascadia CoPes Hub Ground Motions and
Tsunami Sources](https://depts.washington.edu/ptha/CHTuser/docs/seismic-and-tsunami-sources/)
can be found on this DesignSafe website:

**TODO: Add this link, and instructions, once the USGS review is
complete. (We hope before 9/4/26.)

The nc files have been compressed so the whole zip file is about 1GB, and it
unzips to a directory `dtopofiles_nc` with roughly the same size containing 
36 netCDF files with names like `BL10D.nc`. 
See [Cascadia CoPes Hub Ground Motions and Tsunami
Sources](https://depts.washington.edu/ptha/CHTuser/docs/seismic-and-tsunami-sources/)
for more description of these sources, and the naming convention used for
the 36 events in the logic tree.

Unzip this directory and move `dtopofiles_nc` to be a subdirectory of
the `dtopo` directory.

Each file has the cumulative vertical deformation `dz` on a 2D surface grid
with roughly 2 km (?) spacing, at times 10, 20, 30, ... seconds following
the start of the rupture, going up to times ranging from 400 to 500 seconds
depending on the event.

If you want to specify an instantaneous rupture at some time (e.g. 1 second)
with the entire vertical deformation, `dz` from the last time in the .nc
file is the final static deformation. 

The Jupyter notebook `dtopo/LoadSampleSource.ipynb` (found in the
[dtopo directory of the github
repository](https://github.com/rjleveque/LagoonCreekTsunami/tree/main/dtopo)
illustrates how to read a
netCDF file and could be adapted to write it back out in whatever format
your software requires.  Here is a
[rendered version of the notebook](LoadSampleSource.html) that includes
some plots.



