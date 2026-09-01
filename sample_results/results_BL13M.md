(sample_results_BL13M)=
# Sample Results for BL13M

The plots below show the gauge output for the 5 synthetic gauges, for
the event `BL13M`, for both the kinematic (KinOkada) and static (Okada for the
final deformation) ruptures.

Note that the results are very similar except for the timing: waves arrive
earlier for the "instant" version where the total deformation happens at time
1 second.

## Gauge locations

If you want to put synthetic gauges at the same locations as shown in the
plots below for comparison, the coordinates are found in
[](#gauge_locations) and that page also shows Google Earth
images with their locations.



## Zip file of sample gauge output

Download this zip file of the time series if you want to plot them together
with your own results.

https://depts.washington.edu/ptha/CopesHubTsunamis/LagoonCreek/files/LeVeque_v4.zip

The files included in this zip file are in the format needed for comparing
results on the webtool described in the next section, and consist of a header
followed by lines with three columns for the time series at the gauge:

    time (seconds), depth (m), surface elevation (m)



## Web tool for comparing results


See the [](#webtool) page for instructions on using a webtool to compare
your results with the sample results computed with GeoClaw, or with
results computed by other users with different software packages.

You are not required to use this tool, but it is something we are experimenting
with for future use in benchmarking workshops and we would also be happy
to get feedback on how well it works.


## Sample plots

The plots and animations below were computed using the GeoClaw software
(version 5.14.0) with the setup archived in the github repository
in the directory [LagoonCreekTsunamis/geoclaw_run](

### Water depth
The first set of plots shows the **water depth** at each gauge. Note that
gauges 100, 40 are offshore (at water depths of roughly 100m and 40m), while
gauges 1, 2, 3 are onshore.  See [](#LagoonCreekTopo) for figures showing
their locations.

Note that the water depth does not change during the earthquake itself,
since the water moves up and down with the land initially.

:::{figure} ../geoclaw_run/compare_BL13M_depth.png
:width: 600
:::

### Surface elevation

The next set of plots shows the surface elevation `eta = B + h` where `B` is
the topography (which varies with time during the rupture) and `h` is the
water depth. (On dry land where `h = 0`, the surface is simply `B`, the land
surface elevation.)

Note that the KinOkada (kinematic rupture) plots illustrate the co-seismic
subsidence of the land (and water surface) during the earthquake.
In the "instant" ruptures this motion takes place in the first 1 second
and is hard to see on these plots.


:::{figure} ../geoclaw_run/compare_BL13M_eta.png
:width: 600
:::


## Animations

The animations below were made using GeoClaw and may be useful for
comparing against your results.
(To bring up the Loop Controls, click the middle mouse button or 2-finger click.)

### BL13M Kinematic Okada Source

:::{dropdown} Animation of BL13M generation and propagation in Ocean
:close:
```{figure} ../geoclaw_run/BL13M_fgout01_animation.mp4
:width: 600px
:align: center
```
:::

:::{dropdown} Animation of BL13M inundation of Lagoon Creek
:close:
```{figure} ../geoclaw_run/BL13M_fgout02_animation.mp4
:width: 600px
:align: center
```
:::

### BL13M Instantaneous Okada Source

:::{dropdown} Animation of BL13M_instant generation and propagation in Ocean
:close:
```{figure} ../geoclaw_run/BL13M_instant_fgout01_animation.mp4
:width: 600px
:align: center
```
:::


:::{dropdown} Animation of BL13M_instant inundation of Lagoon Creek
:close:
```{figure} ../geoclaw_run/BL13M_instant_fgout02_animation.mp4
:width: 600px
:align: center
```
:::