import mne
import matplotlib.pyplot as plt
from pathlib import Path
from src.preprocessing import bandpass_filter, auto_notch_filter
from src.features import compute_all_band_powers

def load_and_process(filepath, channel):
    """EDF dosyasını oku, filtrele, seçilen kanalı döndür."""
    raw = mne.io.read_raw_edf(filepath, preload=True, verbose=False)
    fs = int(raw.info["sfreq"])
    signal = raw.get_data(picks=[channel]).ravel()
    
    filtered = bandpass_filter(signal, lowcut=1, highcut=40, fs=fs)
    cleaned = auto_notch_filter(filtered, fs)
    
    return cleaned, fs

if __name__ == "__main__":
    
    file_open = "data/S001R01.edf"   
    file_closed = "data/S001R02.edf" 

 
    channels = ["O1..", "O2..", "Oz..", "Pz..", "Cz.."]

    
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    print("=== Alpha Power Comparison (Eyes Open vs Eyes Closed) ===\n")

    alpha_open = []
    alpha_closed = []

    for ch in channels:
        sig_open, fs = load_and_process(file_open, ch)
        sig_closed, _ = load_and_process(file_closed, ch)

        powers_open = compute_all_band_powers(sig_open, fs)
        powers_closed = compute_all_band_powers(sig_closed, fs)

        alpha_open.append(powers_open["alpha"])
        alpha_closed.append(powers_closed["alpha"])

        print(f"Channel {ch}:")
        print(f"  Open   -> Alpha: {powers_open['alpha']:.6e}")
        print(f"  Closed -> Alpha: {powers_closed['alpha']:.6e}")
        if powers_open['alpha'] > 0:
            ratio = powers_closed['alpha'] / powers_open['alpha']
            print(f"  Ratio  -> Closed/Open = {ratio:.2f}x\n")
        else:
            print("  Ratio  -> Not defined (open alpha = 0)\n")

 
    x = range(len(channels))
    width = 0.35

    plt.figure(figsize=(8, 5))
    plt.bar([i - width/2 for i in x], alpha_open, width, label="Eyes Open")
    plt.bar([i + width/2 for i in x], alpha_closed, width, label="Eyes Closed")

    plt.xticks(x, channels)
    plt.ylabel("Alpha Power")
    plt.title("Alpha Band Power: Eyes Open vs Eyes Closed")
    plt.legend()
    plt.tight_layout()

   
    out_path = results_dir / "alpha_compare.png"
    plt.savefig(out_path)
    plt.show()

    print(f"\nGraph saved: {out_path.resolve()}")
