# EEG Preprocessing & Alpha Band Analysis

Bu repo, EEG (Electroencephalography) sinyalleriyle çalışmayı öğrenme yolculuğumun bir parçası.  
Amacım, ham EEG verilerini açıp anlamlı hale getirmek, onları temizlemek, görselleştirmek ve küçük deneylerle beyin dalgalarının doğasını keşfetmek.  

İlk hedefim: **göz açık vs. göz kapalı** durumunda oksipital kanallarda **alpha bandı (8–12 Hz)** farkını gözlemlemekti.  
Ve bu hedef gerçekleşti → göz kapalı durumda alpha gücünün kat kat arttığını bu pipeline sayesinde gördüm 🚀  

---

## 🎯 Projenin Amacı
- **Öğrenme odaklı**: Sıfırdan EEG işleme pipeline’ı kurmak.  
- **Basit ama güçlü**: Bandpass, notch filtre, PSD, band power gibi temel taşları anlamak.  
- **Bilimsel doğrulama**: Literatürdeki en klasik bulguyu (göz kapalı → alpha artışı) kodla yeniden üretmek.  

---

## 📂 Proje Yapısı
```
EEG_Project/
│
├── data/                       # .edf dosyaları (örnek: PhysioNet EEGMMI)
├── src/                        # modüller
│ ├── preprocessing.py          # filtreler (bandpass, notch)
│ ├── visualization.py          # zaman & frekans çizimleri
│ └── features.py               # band power hesaplama
├── results/                    # kaydedilen görseller
│ └── alpha_compare.png
├── main.py                     # temel pipeline (tek kanal demo)
└── compare_alpha_multi.py      # göz açık-kapalı multi-kanal kıyaslama
```

## 🔧 Kurulum
```bash
git clone https://github.com/<kullanıcı-adın>/EEG_Project.git
cd EEG_Project
pip install -r requirements.txt
```

## ▶️ Kullanım
1. Temel pipeline çalıştırma
```bash
python main.py
```
Ham veriyi okur, filtreler ve zaman/frekans grafikleri üretir.

2. Alpha bandı karşılaştırma (multi-kanal)
```bash
python compare_alpha_multi.py
```

## 📊 Örnek Sonuç
Oksipital kanallarda (O1.., O2.., Oz..), göz kapalı durumda alpha gücü göz açığa göre 15–17 kat arttı.
Bu, EEG araştırmalarının temel doğrulamalarından biridir ve pipeline’ımın çalıştığını gösteriyor.

![Alpha Comparison](results/alpha_compare.png)


## 📚 Öğrenme Notlarım
- Preprocessing neden önemli?
Ham EEG’de elektrik paraziti, göz kırpma artefaktları ve düşük frekans kaymaları çok fazla.
Bandpass ve notch filtre uygulamadan doğru analiz yapmak mümkün değil.

- Zaman vs. frekans
Zaman domeninde EEG dalgaları karmaşık görünüyor.
Ama PSD grafiğine geçince frekans bantlarının gücü çok daha anlaşılır hale geliyor.

- Alpha farkı deneyimlemek
Kendi pipeline’ımla göz açık/kapalı alpha farkını görmek inanılmaz motive edici oldu.
Bu, literatürde okuduğum şeyin kendi kodumda yeniden üretimi.

## 📦 Bağımlılıklar
- Python 3.9+ önerilir  
- NumPy  
- SciPy  
- Matplotlib  
- MNE  

Kurulum:
```bash
pip install -r requirements.txt
```

## ✨ Gelecek Çalışmalar
- Artefakt tespiti (örneğin göz kırpma → frontal kanallarda büyük spike’lar)
- Çoklu kanal topomap (beyin yüzeyinde renkli aktivite haritası)
- ML tabanlı basit sınıflandırıcı (örneğin motor imagery denemeleri)

## 📚 Kaynak
- PhysioNet EEG Motor Movement/Imagery Dataset

