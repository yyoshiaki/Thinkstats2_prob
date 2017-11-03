import pandas as pd

def Mode(hist):
    d_hist = hist.d
    ser_hist = pd.Series([v for v in d_hist.values()])
    ser_hist.index = [k for k in d_hist.keys()]
    return ser_hist.max()

def AllModes(hist):
    d_hist = hist.d
    ser_hist = pd.Series([v for v in d_hist.values()])
    ser_hist.index = [k for k in d_hist.keys()]
    return list(ser_hist.sort_values(ascending=False).index), list(ser_hist.sort_values(ascending=False))