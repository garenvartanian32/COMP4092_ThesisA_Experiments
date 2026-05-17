def schedule(func, time, channel="default"):
    try:
        _jobs[channel].stop()
    except (AttributeError, KeyError):
        pass
    timer = QtCore.QTimer()
    timer.setSingleShot(True)
    timer.timeout.connect(func)
    timer.start(time)
    _jobs[channel] = timer