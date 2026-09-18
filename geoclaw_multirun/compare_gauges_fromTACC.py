from pylab import *
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

gauge_plotdir = './gauge_plots'
os.system(f'mkdir -p {gauge_plotdir}')



events = array(all_events)

for gaugeno in [1,2,3,40,100]:
    for event in events[9:]:
        fname_gauge = f'{gauges_dir}/{event}_gauge{gaugeno:05d}.txt'
        #print(fname_gauge)
        gauge_data = loadtxt(fname_gauge, comments='#', skiprows=15)
        t = gauge_data[:,0]
        h = gauge_data[:,1]

        label1 = f'{event} - KinOkada'
        label2 = f'{event} - Okada instant'

        figure(500,figsize=(13,5))
        clf()
        plot(t/60., h, 'b', label=label1)

        fname_gauge = f'{gauges_dir}/{event}_instant_gauge{gaugeno:05d}.txt'
        #print(fname_gauge)
        gauge_data = loadtxt(fname_gauge, comments='#', skiprows=15)
        t = gauge_data[:,0]
        h = gauge_data[:,1]
        plot(t/60., h, 'r', label=label2)

        legend(loc='upper right')
        xlim(0,50)
        #ylim(-2,4)
        grid(True)
        xlabel('Minutes after earthquake')
        ylabel('meters')

        title(f'{event} --- Gauge {gaugeno} water depth')
        fname_png = f'{gauge_plotdir}/{event}_gauge{gaugeno:05d}.png'
        savefig(fname_png)
        print('Created ',fname_png)


