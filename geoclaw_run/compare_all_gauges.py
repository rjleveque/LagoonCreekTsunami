from pylab import *
from clawpack.pyclaw.gauges import GaugeSolution

event = 'BL13M'
#outdirs = '/Users/rjl/scratch/CHTuser/sites/LagoonCreek/multirun/geoclaw_outputs/'
outdir1 = f'_output_{event}'
label1 = f'{event} - KinOkada'
outdir2 = f'_output_{event}_instant'
label2 = f'{event} - Okada instant'

#outdir2 = f'_output_{event}_seismic'
#label2 = f'{event} - Seismic kinematic'

if 0:
    qoi = 'Surface elevation'
    iqoi = -1
else:
    qoi = 'Water depth'
    iqoi = 0

fig,axs = subplots(5,1,figsize=(10,9), sharex=True)

#clf()
for kax,gaugeno in enumerate([100, 40, 1, 2, 3]):

    ax = axs[kax]

    gauge1 = GaugeSolution(gauge_id=gaugeno, path=outdir1)
    gauge2 = GaugeSolution(gauge_id=gaugeno, path=outdir2)


    ax.plot(gauge1.t/60., gauge1.q[iqoi,:], 'b', label=label1)
    ax.plot(gauge2.t/60., gauge2.q[iqoi,:], 'r', label=label2)


    ax.legend(loc='upper right', title=f'Gauge {gaugeno}', fontsize=9)
    
    #ylim(-2,4)
    ax.grid(True)
    ax.set_ylabel('meters')

    
axs[0].set_title(f'Gauge {gaugeno} comparison of {qoi}')
axs[-1].set_xlim(0,60)
axs[-1].set_xlabel('Minutes after earthquake')
tight_layout()