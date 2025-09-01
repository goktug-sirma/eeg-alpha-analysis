import mne
from src.preprocessing import bandpass_filter, auto_notch_filter
from src.visualization import plot_signal, plot_psd_with_notch
from src.features import compute_all_band_powers   # <-- YENİ EKLENDİ

# -------------------------------
# 1. VERİYİ YÜKLE
# -------------------------------
raw = mne.io.read_raw_edf("data/S001R01.edf", preload=True)

# Kayıt hakkında bilgi yazdır (kanallar, sampling rate vs.)
print(raw.info)

# -------------------------------
# 2. KANAL SEÇ
# -------------------------------
fs = int(raw.info["sfreq"])              # örnekleme frekansı (Hz)
signal = raw.get_data(picks=[0]).ravel() # seçilen kanalın sinyali

# -------------------------------
# 3. HAM VERİYİ GÖRSELLEŞTİR
# -------------------------------
plot_signal(signal, fs, title="Raw EEG (Channel 0)")
plot_psd_with_notch(signal, fs)

# -------------------------------
# 4. BANDPASS FİLTRE UYGULA (1–40 Hz)
# -------------------------------
filtered = bandpass_filter(signal, lowcut=1, highcut=40, fs=fs)
plot_signal(filtered, fs, title="After Bandpass (1-40 Hz)")

# -------------------------------
# 5. NOTCH FİLTRE UYGULA (50 Hz parazit için)
# -------------------------------
cleaned = auto_notch_filter(filtered, fs)
plot_signal(cleaned, fs, title="After Notch Filter")
plot_psd_with_notch(cleaned, fs)

# -------------------------------
# 6. BAND POWER HESAPLA  <-- YENİ BLOK
# -------------------------------
powers = compute_all_band_powers(cleaned, fs)
print("Band powers:", powers)
