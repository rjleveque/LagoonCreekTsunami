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

## Maximum inundation depth at Gauge 2

One way to compare the events is to plot the maximum depth over the simulation
at one location, e.g. Gauge 2.  This plot shows this value for each event
after sorting from smallest to largest. The width of each bar is proportional
to the weight assigned to the event in the logic tree shown at
[Cascadia CoPes Hub Ground Motions and Tsunami
Sources](https://depts.washington.edu/ptha/CHTuser/docs/seismic-and-tsunami-sources/).

:::{figure} ../geoclaw_multirun/LagoonCreek_Gauge00002_depth_bars_260915.png
:width: 600
:::

More discussion to appear...