import mne
from src.preprocessing import bandpass_filter, auto_notch_filter
from src.visualization import plot_signal, plot_psd_with_notch
from src.features import compute_all_band_powers   

raw = mne.io.read_raw_edf("data/S001R01.edf", preload=True) 
print(raw.info)

fs = int(raw.info["sfreq"])         
signal = raw.get_data(picks=[0]).ravel()

plot_signal(signal, fs, title="Raw EEG (Channel 0)")
plot_psd_with_notch(signal, fs)

filtered = bandpass_filter(signal, lowcut=1, highcut=40, fs=fs)
plot_signal(filtered, fs, title="After Bandpass (1-40 Hz)")

cleaned = auto_notch_filter(filtered, fs)
plot_signal(cleaned, fs, title="After Notch Filter")
plot_psd_with_notch(cleaned, fs)

powers = compute_all_band_powers(cleaned, fs)
print("Band powers:", powers)
