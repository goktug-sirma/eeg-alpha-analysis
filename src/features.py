import numpy as np
from scipy.signal import welch

def compute_band_power(data, fs, band, nperseg=None):
    
    if nperseg is None:
        nperseg = fs * 2
    
    freqs, psd = welch(data, fs, nperseg=nperseg)
    
    low, high = band
    idx_band = np.logical_and(freqs >= low, freqs <= high)
    
    band_power = np.trapz(psd[idx_band], freqs[idx_band])
    
    return band_power

def compute_all_band_powers(data, fs):

    bands = {
        "delta": (1, 4),
        "theta": (4, 8),
        "alpha": (8, 12),
        "beta": (12, 30),
        "gamma": (30, 40)
    }
    
    powers = {}
    for name, (low, high) in bands.items():
        powers[name] = compute_band_power(data, fs, (low, high))
    return powers
