
(webtool)=
# Code Verification Platform webtool for comparison

[This webpage](https://det.cascadiaquakes.org/?benchmark_id=TSHA-BP1#)
provides a tool for comparing your computed results with results obtained
by others.

:::{note}
Still under development and may change before the workshop.  This tool
is being developed by the CRESCENT software engineers and the
[Dynamic Rupture, Earthquake Cycle, and Tsunamis Working Group](https://cascadiaquakes.org/det/).

Note that some of the terminology (e.g. "receiver") was developed for
the original application to seismic modeling, not tsunami gauges.
:::

## To view archived results

To view results on
[the comparison webpage](https://det.cascadiaquakes.org/?benchmark_id=TSHA-BP1#)
that have been uploaded by others, do the following:
- Select one or more of the datasets from the "Dataset selection"
menu on the left of the page,
- Choose a "file type" (either `BL13M` for the kinematic
source or `BL13M_instant` for the instantaneous source),
- Choose a "receiver" (one of the 5 gauges), 
- Click on "Show graphs"

Then plots of the depth and surface elevation at this gauge should
appear on the right.

## To quickly view/compare one of your own results

If you want to quickly look at a single gauge from your own results and
see how it compares to any or all of the archived results, you can use
the "Upload File" button to upload a single `.txt` file with the format
described below.  Then select one or more datasets to compare to and make
sure you select the "file type" corresponding to your own run (kinematic or
instant) and the "receiver" corresponding to the gauge number of the file
you upload.  Then "Show graphs" should show the comparison.

When you do it this way, you can only upload and examine one gauge at a time
and no data is stored on the server.

## To upload a set of results and have them archived

- Create a file for each event/gauge that you wish to include (up to 10 if
you include one for each gauge from both the kinematic and instant events)
in a directory titled `ModelerName_Version` and then zip this directory.

- Click on the "Uploader" button in the top right corner.
If this is the first time you upload, you will need to request access and
wait for that to be processed.

- Select Benchmark ID TSHA-BP1
- Drop files or Browse files
- Wair for it to say "File processed successfully" and then "View processing
summary" to check if there are any files with errors.

## File format

The time series for each gauge should be in a separate file with names like
`BL13M_gauge00001.txt` or `BL13M_instant_gauge00001.txt`.  You can include
a header with as many lines as you like, each line starting with `#`.
The format below is recommended.

    # Benchmark problem (TSHA-BP1)
    # Code name
    # Code version (optional)
    # Modeler
    # Date
    # Tsunami Source (event)
    # Gauge number
    # Gauge location (optional)
    # Anything else you think is relevant, e.g. resolution used (optional)

Then there should be a line
    t depth surf
followed by a line for each time in the time series with values
time, water depth, and surface elevation of the water (or of the land if dry).

Here's an example file `BL13M_instant_gauge00040.txt`:

    # TSHA-BP1
    # Code name: GeoClaw
    # Version: 5.14.0
    # Modeler: Randy LeVeque
    # Date: 2026-08-29
    # Tsunami Source: BL13M_instant
    # Gauge 40
    # Gauge location:  -124.200000, 41.600000
    # v4: Computed with AMR using 1/3" grids at finest level
    # onshore, where refinement is forced starting at time 0.
    # After fixing the 1s topo to use the 2025 CRM vol 7.

    t depth surf

        0.000     40.188      0.000
        5.434     40.188     -0.852
        10.665     40.188     -0.852
        15.896     40.188     -0.852
        21.126     40.188     -0.852
        etc.