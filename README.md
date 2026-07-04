# 📞 Vornexx Call Spam Tool

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-orange)
![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Linux%20%7C%20Windows-red)

Telz API kullanarak gelişmiş çağrı spam aracı. Renkli arayüz, animasyonlu yüklemeler ve çoklu arama desteği ile profesyonel bir deneyim sunar.

## ⚠️ Yasal Uyarı

**Bu araç yalnızca eğitim amaçlıdır!** Bu yazılımın kötüye kullanımı yasa dışıdır. Geliştirici, bu aracın yanlış kullanımından doğacak hukuki sorumlulukları kabul etmez. Sadece kendi numaralarınız veya açık izin aldığınız numaralar üzerinde test yapın.

## ✨ Özellikler

- 🎨 **Renkli Terminal Arayüzü** - Colorama ile geliştirilmiş görsel arayüz
- 🔄 **Animasyonlu Yüklemeler** - Spinner ve progress bar animasyonları
- 📱 **Çoklu Platform Desteği** - Termux, Linux ve Windows uyumlu
- 🚦 **Rate Limiting** - Akıllı hız sınırlandırma sistemi
- 📊 **Detaylı İstatistikler** - API çağrıları ve arama istatistikleri
- ⚙️ **Özelleştirilebilir Ayarlar** - Bekleme süresi, animasyon hızı vb.
- 📝 **Debug Modu** - Hata ayıklama için detaylı log
- 🎯 **Tekli ve Çoklu Arama** - Liste ile toplu arama desteği

## 🚀 Kurulum

### Gereksinimler

- Python 3.6 veya üzeri
- pip (Python paket yöneticisi)

---

## 📱 Termux'a Sıfırdan Kurulum (Android)

### Adım 1: Termux'u Yükleyin

Termux'u F-Droid'den indirin (Google Play'deki sürüm güncel değil):
- [F-Droid'den Termux İndir](https://f-droid.org/repo/com.termux_118.apk)

> ⚠️ **Önemli**: Google Play Store'daki Termux sürümü güncellenmiyor! Mutlaka F-Droid'den indirin.

### Adım 2: Termux'u İlk Kez Başlatın

Termux uygulamasını açın ve aşağıdaki komutları sırayla girin:

```bash
# 1. Termux depolarını güncelleyin
pkg update -y && pkg upgrade -y

# 2. Temel paketleri yükleyin
pkg install -y python python-pip git curl wget nano

# 3. Depolama izni verin (dosya paylaşımı için)
termux-setup-storage
#Gelen sekmede "İzin ver" Seçeneğini seçin

# 4. Python pip'i güncelleyin
pip install --upgrade pip

# 5. Repoyu klonlayın ve klasöre girin
git clone [https://github.com/VornexxBaba/Call-Spam-Vornex.git](https://github.com/VornexxBaba/Call-Spam-Vornex.git)

#Klasörü açın
cd Call-Spam-Vornex

# 6. Gerekli kütüphaneleri yükleyin
pip install requests colorama pyfiglet

# 7. Programı çalıştırın
python3 main.py
