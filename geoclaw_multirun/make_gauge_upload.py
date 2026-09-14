from pylab import *
from clawpack.pyclaw.gauges import GaugeSolution
from pathlib import Path

gaugedir = Path('./geoclaw_gauges_to_upload')
gaugedir.mkdir(parents=True, exist_ok=True)
gaugedir = gaugedir.resolve()
print(f'gaugedir = {gaugedir}')

outputs_dir = 'geoclaw_outputs'

header_format = """
# TSHA-BP1
# Code name: GeoClaw
# Version: 5.14.0
# Modeler: Randy LeVeque
# Date: 2026-09-15
# Tsunami Source: {event}
# Gauge {gaugeno}
# Gauge location:  {xg:.6f}, {yg:.6f}
# v4: Computed with AMR using 1/3" grids at finest level
# onshore, where refinement is forced starting at time 0.
# After fixing the 1s topo to use the 2025 CRM vol 7.

t depth surf
"""

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
events = all_events

#events = ['BL13M', 'BL13M_instant']
#events = ['BL13M_instant']

for event in events:

    outdir = f'{outputs_dir}/_output_{event}'
    gaugenos = [1,2,3,40,100]

    for gaugeno in gaugenos:
        gauge = GaugeSolution(gauge_id=gaugeno, path=outdir)
        t = gauge.t
        depth = gauge.q[0,:]
        eta = gauge.q[-1,:]  # always last element, for SWE or Bouss
        xg,yg = gauge.location

        gdata = vstack((t, depth, eta)).T
        fname = gaugedir / f'{event}_gauge{gaugeno:05d}.txt'
        header_info = dict(event=event, gaugeno=gaugeno, xg=xg, yg=yg)
        header = header_format.format(**header_info)
        savetxt(fname, gdata, delimiter=' ', fmt='%10.3f', header=header,
                comments='')
        print('Created ',fname)
