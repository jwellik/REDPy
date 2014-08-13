from tables import *
import numpy as np
import matplotlib.pyplot as plt

"""
These are very brute force plotting; should be replaced with more
"""


def createOrderedWaveformFigure(rtable):
    data = np.zeros((len(rtable), 2000))
    fig = plt.figure(figsize=(12, 6))
    n=-1
    for r in rtable.iterrows():
        n = n+1
        data[n, :] = r['waveform'][r['windowStart']-500:r['windowStart']+1500]
        data[n, :] = data[n, :]/max(data[n, 500:1012])
    
    order = rtable.cols.order[:]
    datao = data[order, :]
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(datao, aspect='auto', vmin=-1, vmax=1, interpolation='nearest', cmap='RdBu')

def createCMatrixFigure(rtable, ctable):
    
    C = np.zeros((len(rtable),len(rtable)))
    id1 = ctable.cols.id1[:]
    id2 = ctable.cols.id2[:]
    
    # Convert id to row
    rtable_ids = rtable.cols.id[:]
    r = np.zeros((max(rtable_ids)+1,)).astype('int')
    r[rtable_ids] = range(len(rtable_ids))
    C[r[id1], r[id2]] = ctable.cols.ccc[:]
    C = C + C.T + np.eye(len(C))
    Co = C[order, :]
    Co = Co[:, order]

    # Plot the C matrices (saturated below 0.65)
    # Left is ordered by time
    # Right is ordered by cluster ordering
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 2, 1)
    ax.imshow(C, aspect='auto', vmin=0.65, vmax=1, interpolation='nearest')
    ax = fig.add_subplot(1, 2, 2)
    ax.imshow(Co, aspect='auto', vmin=0.65, vmax=1, interpolation='nearest')

