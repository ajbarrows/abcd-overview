import numpy as np
from math import gamma

def abcd_hrf(t_r=0.8, oversampling=1, time_length=30, A=1, 
             delay=6, undershoot=16, dispersion=1, 
             u_dispersion=1, ratio=1/6):

    dt = t_r / oversampling
    X = np.arange(0, time_length, dt)

    peak_gamma = (X ** (delay-1) * np.exp(-dispersion*X) * dispersion**delay)
    peak_gamma = peak_gamma / gamma(delay)

    undershoot_gamma = (X ** (undershoot-1) * np.exp(-u_dispersion*X) * u_dispersion**undershoot)
    undershoot_gamma = undershoot_gamma / gamma(undershoot)

    hrf = A * (peak_gamma - ratio * undershoot_gamma)
    hrf /= hrf.sum()

    return hrf