Sample Gauge output for event BL13M

These are for the KinOkada version with no subevents, and also for the
"instant" version where the final static deformation is used as an
instantaneous rupture at time t = 1 second.

For more information about these sources, see
    https://depts.washington.edu/ptha/CHTuser/docs/seismic-and-tsunami-sources/

The results were computed using GeoClaw version 5.14.0 and the code used
is in the Github repository 
    https://github.com/rjleveque/LagoonCreekTsunami

See also the documentation pages built from that repository, at
    https://depts.washington.edu/ptha/CopesHubTsunamis/LagoonCreek/

------------

The gauge results are in ascii text files in the GeoClaw format.
    https://www.clawpack.org/gauges.html

Following 4 lines of header, each line of the file has columns:
    AMR level, time (seconds), h, hu, hv, eta

where h is the water depth (meters), (hu,hv) the momenta,
and eta = h+B is the surface elevation.

Note that that the ground elevation can be computed as B = eta - h 
and varies with time during the co-seismic deformation.

AMR level is the adaptive mesh refinement level of the finest resolution
grid that was covering the gauge at each time.  In this GeoClaw simulation,
    level 4 = 3"
    level 5 = 1"
    level 6 = 1/3"



