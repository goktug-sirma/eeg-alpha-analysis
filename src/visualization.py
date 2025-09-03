import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

def plot_signal(data, fs, title="EEG Signal"):
   
    times = np.arange(len(data)) / fs  
    plt.figure(figsize=(12, 4))
    plt.plot(times, data, color='blue')
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (µV)")
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_psd(data, fs, title="Power Spectral Density"):

    freqs, psd = welch(data, fs, nperseg=fs*2)  
    plt.figure(figsize=(12, 4))
    plt.semilogy(freqs, psd, color='red')  
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power")
    plt.title(title)
    plt.grid(True)
    plt.xlim(0, 80) 
    plt.show()

def plot_psd_with_notch(data, fs, notch_freq=None):
    
    freqs, psd = welch(data, fs, nperseg=fs*2)
    plt.figure(figsize=(12, 4))
    plt.semilogy(freqs, psd, color='red')
    if notch_freq:
        plt.axvline(notch_freq, color='black', linestyle='--', label=f"{notch_freq} Hz Noise")
        plt.legend()
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power")
    plt.title("Power Spectral Density with Notch Marked")
    plt.grid(True)
    plt.xlim(0, 80)
    plt.show()
