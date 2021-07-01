# Import libraries
from redpitaya.overlay.mercury import mercury as overlay

from bokeh.io import push_notebook, show, output_notebook
from bokeh.models import HoverTool, Range1d, LinearAxis, LabelSet, Label
from bokeh.plotting import figure, output_file, show
from bokeh.resources import INLINE
output_notebook(resources=INLINE)

import numpy as np

# Initialize fpga modules
fpga = overlay()
gen0 = fpga.gen(0)
osc = [fpga.osc(ch, 1.0) for ch in range(fpga._MNO)]

# Configure OUT1 generator channel
gen0.amplitude = 0.5
gen0.offset = 0.5
gen0.waveform = gen0.sawtooth(0.5)
gen0.frequency = 2000
gen0.start()
gen0.enable = True
gen0.trigger()

# R1 resistor value
R1 = 10

# Configure IN1 and IN2 oscilloscope input channels
for ch in osc:
    ch.filter_bypass = True
    # data rate decimation
    ch.decimation = 10
    # trigger timing [sample periods]
    N = ch.buffer_size
    ch.trigger_pre = 0
    ch.trigger_post = N
    # osc0 is controlling both channels
    ch.sync_src = fpga.sync_src["osc0"]
    ch.trig_src = fpga.trig_src["osc0"]
    # trigger level [V], edge ['neg', 'pos'] and holdoff time [sample periods]
    ch.level = 0.5
    ch.edg = 'pos'
    ch.holdoff = 0

# Initialize diode current and voltage
V = I = np.zeros(N)

# Plotting
hover = HoverTool(mode='vline', tooltips=[("V", "@x"), ("I", "@y")])
tools = "wheel_zoom, box_zoom, reset, pan"
p = figure(plot_height=500, plot_width=900,
           title="XY plot of diodes VI characteristic",
           toolbar_location="right",
           tools=(tools, hover))
p.xaxis.axis_label = 'Voltage in V'
p.yaxis.axis_label = 'Current in mA'
r = p.line(V, I, line_width=1, line_alpha=0.7, color="blue")

# get and explicit handle to update the next show cell
target = show(p, notebook_handle=True)
