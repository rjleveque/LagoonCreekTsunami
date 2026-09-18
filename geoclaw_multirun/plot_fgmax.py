import sys
if 'matplotlib' not in sys.modules:
    import matplotlib
    matplotlib.use('Agg')  # Use an image backend

from pylab import *

import os,sys,glob,zipfile,shutil
from clawpack.clawutil.data import ClawData
from clawpack.geoclaw import topotools, dtopotools
from clawpack.visclaw import colormaps, gridtools
import matplotlib as mpl
from matplotlib import colors
from clawpack.amrclaw import region_tools
from clawpack.visclaw import plottools
from clawpack.visclaw import geoplot
from clawpack.geoclaw import kmltools, fgmax_tools
import sys

import os

depths = ['D','M','S']
    
# buried_locking events:
all_events = [f'BL10{depth}' for depth in depths] \
           + [f'BL13{depth}' for depth in depths] \
           + [f'BL16{depth}' for depth in depths] \
    
# add random events:
all_events += [e.replace('L','R') for e in all_events]

# add Frontal Thrust events:
all_events += [e.replace('B','F') for e in all_events]

all_events.sort()
print(f'all_events contains {len(all_events)} events')

#gauges_dir = 'geoclaw_gauges_to_upload'
gauges_dir = 'geoclaw_gauges_all_events'

fgmax_plotdir = './fgmax_plots'
os.system(f'mkdir -p {fgmax_plotdir}')

events = array(all_events)

outdirs = 'geoclaw_outputs'

#for event in events:
for event in ['FL10D']:

    fgmax = fgmax_tools.FGmaxGrid()
    fgmax.outdir = f'{outdirs}/_output_{event}'

    # read the input data used for this run:
    data_file = os.path.join(fgmax.outdir, 'fgmax_grids.data')
    fgmax.read_fgmax_grids_data(fgno=1, data_file=data_file)

    # read fgmax results:
    fgmax.read_output()

    topo = topotools.Topography('../topo/LagoonCreek13s.asc', topo_type=3)
    topo_fcn = topo.make_function()
    fgmax.B0 = topo_fcn(fgmax.X, fgmax.Y)

    onshore = fgmax.B0 > 0
    h_onshore = where(onshore, fgmax.h, nan)
    zeta = where(onshore, fgmax.h, fgmax.h+fgmax.B0)

    fg_image = imread('../topo/LagoonCreekTopo.jpg')
    fg_extent = [-124.12, -124.087, 41.578, 41.608]


    zetamax = nanmax(zeta)

    clines = [0.01] + list(arange(1,zetamax,3))
    nlines = len(clines)
    n1 = int(floor((nlines-1)/2.))
    n2 = nlines - 1 - n1
    Green = hstack([linspace(1,1,n1),linspace(1,0,n2)])
    Red = hstack([linspace(0,0.8,n1), ones(n2)])
    Blue = hstack([linspace(1,0.2,n1), zeros(n2)])
    Alpha = 0.5*ones(nlines)  # transparency
    colors = list(zip(Red,Green,Blue,Alpha))

    figure(figsize=(8,8))
    imshow(fg_image, extent=fg_extent)

    contourf(fgmax.X,fgmax.Y,h_onshore,clines,colors=colors)

    colorbar(extend='max', label='meters')
    title('Max water depth onshore')

    # fix axes:
    ticklabel_format(style='plain',useOffset=False)
    xticks(rotation=20)
    gca().set_aspect(1./cos(fgmax.Y.mean()*pi/180.));

    fname = f'{fgmax_plotdir}/{event}_fgmax.png'
    savefig(fname)
    print('Created ',fname)

if 0:
    clines_zeta = [0.01] + list(arange(1,zetamax,2))
    colors_zeta = geoplot.discrete_cmap_1(clines_zeta)

    figure(figsize=(8,6))
    imshow(fg_image, extent=fg_extent)
    contourf(fgmax.X,fgmax.Y,zeta,clines_zeta,colors=colors_zeta)

    colorbar(extend='max', label='meters')
    contour(fgmax.X,fgmax.Y,fgmax.B0,[0.],colors='b', linewidths=0.7)
    title('zeta = max depth onshore / max eta offshore')

    # fix axes:
    ticklabel_format(style='plain',useOffset=False)
    xticks(rotation=20)
    gca().set_aspect(1./cos(fgmax.Y.mean()*pi/180.));