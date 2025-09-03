import numpy as np
from scipy.signal import butter, lfilter, welch

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def auto_notch_filter(data, fs, quality=30):
    freqs, psd = welch(data, fs)
    peak_freq = freqs[np.argmax(psd)]
    
    if 49 <= peak_freq <= 51:
        return notch_filter(data, 50, fs, quality)
    elif 59 <= peak_freq <= 61:
        return notch_filter(data, 60, fs, quality)
    else:
        return data

def notch_filter(data, freq, fs, quality=30):
    from scipy.signal import iirnotch
    w0 = freq / (fs / 2)
    b, a = iirnotch(w0, quality)
    y = lfilter(b, a, data)
    return y
