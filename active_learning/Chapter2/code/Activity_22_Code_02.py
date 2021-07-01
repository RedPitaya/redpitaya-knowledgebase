# Measuring I, V  and re-plotting
while True:
    # reset and start
    osc[0].reset()
    osc[0].start()

    # wait for data
    while (osc[0].status_run()):
        pass
    V0 = osc[0].data(N-100)*10  # IN1 signal
    V1 = osc[1].data(N-100)*10  # IN2 signal
    I = ((V0-V1)/R1)*1E3        # 1E3 convert to mA
    r.data_source.data['x'] = V0
    r.data_source.data['y'] = I

    push_notebook(handle=target)
