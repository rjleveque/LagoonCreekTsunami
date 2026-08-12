(results_BL13M)=
# Results for BL13M

The plots below show the gauge output for the 5 synthetic gauges, for
the event `BL13M`, for both the kinematic (KinOkada) and static (Okada for the
final deformation) ruptures.


Note that the results are very similar except for the timing: waves arrive
earlier for the "instant" version where the total deformation happens at time
1 second.

## Zip file of sample gauge output

Download this zip file of the time series if you want to plot them together
with your own results.

https://depts.washington.edu/ptha/CopesHubTsunamis/LagoonCreek/files/GaugeResults_BL13M.zip


## Sample plots

### Water depth
The first set of plots shows the water depth at each gauge. Note that
gauges 100, 40 are offshore (at water depths of roughly 100m and 40m), while
gauges 1, 2, 3 are onshore.  See [](#LagoonCreekTopo) for figures showing
their locations.

:::{figure} ../geoclaw_run/compare_BL13M_instant_depth.png
:width: 600
:::

### Surface elevation

The next set of plots shows the surface elevation `eta = B + h` where `B` is
the topography (which varies with time during the rupture) and `h` is the
water depth.

Note that in this figure eta at the onshore gauges shows the land elevation
at these points when `h = 0`, and also shows the difference in the
co-seismic change between the kinematic and instant rupture cases.

:::{figure} ../geoclaw_run/compare_BL13M_instant_eta.png
:width: 600
:::


## Animations

The animations below were made using GeoClaw and may be useful for
comparing against your results.
(To bring up the Loop Controls, click the middle mouse button or 2-finger click.)

:::{dropdown} BL13D generation and propagation in Ocean
:close:
```{figure} ../geoclaw_run/BL13M_fgout01_animation.mp4
:width: 600px
:align: center
```
:::

:::{dropdown} BL13D_instant generation and propagation in Ocean
:close:
```{figure} ../geoclaw_run/BL13M_instant_fgout01_animation.mp4
:width: 600px
:align: center
```
:::

:::{dropdown} BL13D inundation of Lagoon Creek
:close:
```{figure} ../geoclaw_run/BL13M_fgout02_animation.mp4
:width: 600px
:align: center
```
:::

:::{dropdown} BL13D_instant inundation of Lagoon Creek
:close:
```{figure} ../geoclaw_run/BL13M_instant_fgout02_animation.mp4
:width: 600px
:align: center
```
:::