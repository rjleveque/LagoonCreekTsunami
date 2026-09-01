(LagoonCreekTopo)=
# Lagoon Creek Topography files

:::{warning}
The topography for this test problem has been finalized for the webinar
and workshop in September, 2026.

But note that the 1/3 arcsecond topo used near Lagoon Creek dates from
2010 and a newer version is currently under development by NCEI, which
should be available soon.  The newer topography differs
from the 2010 version around Lagoon Creek.

It is also worth noting that present-day topography may not be
suitable if you plan to do modeling with a tsunami source that might
be a good model for the 1700 event, to compare to the paleo data,
since the topography may have changed dramatically since then.  
:::

## zip file with files needed to run the test problem

**This zip file was updated 8/29/26.**

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
Source: https://www.ngdc.noaa.gov/thredds/dodsC/crm/cudem/crm_vol7_2025.nc

**Updated 8/29/26 to use the new 2025 version of CRM volume 7.**

###  `LagoonCreek13s.asc`

1/3" data from the 2010 Regional DEM, with 
`extent = [-124.12, -124.087, 41.578, 41.608]` \
Vertical datum: MHW \
Source: https://www.ngdc.noaa.gov/thredds/dodsC/regional/crescent_city_13_mhw_2010.nc

## Jupyter notebook used to construct this data

The notebook is in the github repository, in `topo/LagoonCreekTopo.ipynb`.
Here is a [rendered version](LagoonCreekTopo.html).

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

Sample gauge output for one event are shown in [](#sample_results_BL13M).

## Gauge locations

If you want to put synthetic gauges at the same locations as shown in the
plots below for comparison, the coordinates are:

:::{table} Gauge locations
:label: gauge_locations
:align: center

| Gauge | longitude | latitude | location |
| --- | --- | --- | --- |
| 1 | -124.102 | 41.596 | on beach |
| 2 | -124.098 | 41.5925 | in lake |
| 3 | -124.0954 | 41.5891 | farther inland |
| 40 | -124.2 | 41.6 | offshore, $\approx$ 40 m depth |
| 100 | -124.38 | 41.59 | offshore, $\approx$ 100 m depth |

:::

