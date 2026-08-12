(LagoonCreekTopo)=
# Lagoon Creek Topography files

The zip file found at:

https://depts.washington.edu/ptha/CopesHubTsunamis/LagoonCreek/files/LagoonCreek_topofiles.zip

contains three topography DEMs at different resolutions that can be used
for this modeling problem, or you can use whatever topography files you
have available or need for your software.  But to get reasonable agreement
with posted results, you will probably need similar resolutions to the
files provided.

## The zip files contains:


### `etopo30sec.asc` 

30 arcsecond etopo 2022 data, `with 
extent = [-138, -121, 37, 52]` \
Source: https://www.ngdc.noaa.gov/thredds/dodsC/global/ETOPO2022/30s/30s_bed_elev_netcdf/ETOPO_2022_v1_30s_N90W180_bed.nc

###  `LagoonCreek1s.asc`

1" data from Coastal Relief Model Volume 7, with 
`extent = [-124.3, -124., 41.5, 41.8]` \
Source: https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol7.nc


###  `LagoonCreek13s.asc`

1/3" data from the 2010 Regional DEM, with 
`extent = [-124.12, -124.087, 41.578, 41.608]` \
Vertical datum: MHW \
Source: https://www.ngdc.noaa.gov/thredds/dodsC/regional/crescent_city_13_mhw_2010.nc


## To do: 

- Add Jupyter notebook that downloads / crops these files.
- Determine if there is better fine grid topo or lidar available.

## Topography extents and gauge locations

The green rectangles below show the extents of the 1" and 1/3" topo and
the location of 2 offshore synthetic gauges (#100 at roughly 100 m depth, and
#40 at roughly 40 m depth).

:::{figure} topo_gauges.jpg
:width: 500
:::

The zoomed view below shows the 1/3" topo extent and
the location of 3 onshore gauges #1, 2, 3.

:::{figure} topo_gauges_onshore.jpg
:width: 500
:::

Sample gauge output for one event are shown in [](#results_BL13M).