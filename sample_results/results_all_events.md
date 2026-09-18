(sample_results_all)=
# Sample Results for all events

Recently GeoClaw has been run on all the events with the setup archived
in the github repository in the directory
[LagoonCreekTsunamis/geoclaw_multirun](https://github.com/rjleveque/LagoonCreekTsunami/tree/main/geoclaw_multirun).
This page contains a few preliminary results, to be improved in the future.

## Zip file of gauge output

This zip file contains the time series at each of the 5 gauges for all of
the events, if you want to plot them together with your own results:

[geoclaw_gauges_all_events.zip](https://depts.washington.edu/ptha/CopesHubTsunamis/LagoonCreek/files/geoclaw_gauges_all_events.zip)

The files included in this zip file are in the same format as in the zip
file described in the [](#sample_results_BL13M), and consist of a header
followed by lines with three columns for the time series at the gauge:

    time (seconds), depth (m), surface elevation (m)

## Maximum inundation depth at Gauges

One way to compare the events is to plot the maximum depth over the simulation
at one location, e.g. one of the onshore gauges.  
This plots below for each gauge show this value for each event
after sorting from smallest to largest. The width of each bar is proportional
to the weight assigned to the event in the logic tree shown at
[Cascadia CoPes Hub Ground Motions and Tsunami
Sources](https://depts.washington.edu/ptha/CHTuser/docs/seismic-and-tsunami-sources/).

:::{dropdown}Gauge Locations
```{figure} ../topo/topo_gauges_onshore.jpg
:width: 600
```
:::
:::{dropdown}Maximum inundation depth at Gauge 1
```{figure} ../geoclaw_multirun/LagoonCreek_Gauge00001_depth_bars_260915.png
:width: 600
```
:::

:::{dropdown}Maximum inundation depth at Gauge 2
```{figure} ../geoclaw_multirun/LagoonCreek_Gauge00002_depth_bars_260915.png
:width: 600
```
:::

:::{dropdown}Maximum inundation depth at Gauge 3
```{figure} ../geoclaw_multirun/LagoonCreek_Gauge00003_depth_bars_260915.png
:width: 600
```
:::

A few things to note:

- In general the events with 10 in the name (using the Strasser et al 2010
  magnitude-area relationship from the logic tree) have the largest magnitude,
  so it is not surprising that most of these give greater inundation than
  other events.
- FL10D has much greater depths than any other event. This event is Mw 9.2 with
  substantial uplift at the southern end, near Lagoon Creek.
- BR16M and BR16D have little flooding at Gauge 1 and none at Gauges 2 and 3.
  These events have uplift in this region.

Plots of the slip and seafloor deformation for each of the 36 sources can
be found in the Powerpoint slides included in the data distribution.
The pdf version can also be viewed
[here](https://depts.washington.edu/ptha/CopesHubTsunamis/LagoonCreek/files/copes_megathrust_scenarios_tsunami_sources.pdf).

The plots shown above were computed with the Jupyter notebook
`geoclaw_multirun/CompareGaugeMaxima.ipynb`
in the repository.  Here is a
[rendered version of the notebook](../geoclaw_multirun/CompareGaugeMaxima_260917.html).

## PTHA

The 36  Cascadia CoPes Hub Sources
were not originally designed for Probabilistic Tsunami Hazard Assessment (PTHA),
and may not cover the full range of CSZ earthquakes.
Moreover, this is a relatively small set of sources.

However, the relative likelihood of these particular events (as defined by
the weights in the logic tree) sum to 1, and might be viewed as conditional 
probabilities (i.e. given that a major CSZ earthquake occurs, the weight is
the relative probability of each).
These weights can be combined with a presumed annual probability that
such an event occurs in order to obtain an annual probability of each event.
These can then be used (together with tsunami simulations of each event)
to perform PTHA (with the caveats mentioned above).

One typical product of a PTHA analysis is a "hazard curve" that plots the
annual probability that some quantity of interest exceeds a threshold as a
function of that threshold.  These are similar to the plots shown above,
but with annual probability on the vertical axis and require additional
assumptions and a slightly more complicated set of formulas to compute.

For more discussion and an illustration of how a hazard curve could be
computed, see 
[HazardCurveDemo](../geoclaw_multirun/HazardCurveDemo_260917.html),
rendered from the notebook `geoclaw_multirun/HazardCurveDemo.ipynb`
in the repository.
