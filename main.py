#!/usr/bin/env python3

import requests
import json
import time
import uuid
import os
import sys
import random
import threading
from threading import Lock
from datetime import datetime
from collections import defaultdict
import itertools

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_VAR = True
except ImportError:
    COLORAMA_VAR = False
    class Fore:
        GREEN = '\033[92m'
        RED = '\033[31m'
        WHITE = '\033[37m'
        CYAN = '\033[96m'
        YELLOW = '\033[93m'
        MAGENTA = '\033[95m'
        BLUE = '\033[94m'
        BLACK = '\033[30m'
    class Back:
        MAGENTA = '\033[45m'
        BLACK = '\033[40m'
        WHITE = '\033[47m'
        GREEN = '\033[42m'
        RED = '\033[41m'
    class Style:
        BRIGHT = '\033[1m'
        DIM = '\033[2m'
        NORMAL = '\033[22m'

try:
    import pyfiglet
    PYFIGLET_VAR = True
except ImportError:
    PYFIGLET_VAR = False

class AnimasyonluArayuz:
    
    def __init__(self):
        self.animasyon_aktif = True
        self.durum_mesaji = ""
        self.islem_sayaci = 0
        self.basari_sayaci = 0
        self.hata_sayaci = 0
        
    def yukleniyor_animasyonu(self, mesaj="İşlem yapılıyor", sure=3):
        spinner = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
        baslangic = time.time()
        
        while time.time() - baslangic < sure:
            sys.stdout.write(f'\r{Fore.CYAN}{next(spinner)} {mesaj}... {Style.DIM}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'\r{Fore.GREEN}✓ {mesaj} tamamlandı!    \n')
        sys.stdout.flush()
    
    def ilerleme_cubugu(self, yuzde, genislik=40):
        dolu = int(genislik * yuzde / 100)
        bos = genislik - dolu
        
        if yuzde > 66:
            renk = Fore.GREEN
        elif yuzde > 33:
            renk = Fore.YELLOW
        else:
            renk = Fore.RED
        
        cubuk = f"{renk}{'█' * dolu}{Style.DIM}{'░' * bos}"
        sys.stdout.write(f'\r{cubuk} %{yuzde:3.1f}')
        sys.stdout.flush()
    
    def banner_goster(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
        if PYFIGLET_VAR:
            banner = pyfiglet.figlet_format("VORNEXX CALL", font="slant")
            print(f"{Fore.CYAN}{Style.BRIGHT}{banner}")
        else:
            print(f"""
{Fore.YELLOW}██╗░░░██╗░█████╗░██████╗░███╗░░██╗███████╗██╗░░██╗
██║░░░██║██╔══██╗██╔══██╗████╗░██║██╔════╝╚██╗██╔╝
╚██╗░██╔╝██║░░██║██████╔╝██╔██╗██║█████╗░░░╚███╔╝░
░╚████╔╝░██║░░██║██╔══██╗██║╚████║██╔══╝░░░██╔██╗░
░░╚██╔╝░░╚█████╔╝██║░░██║██║░╚███║███████╗██╔╝╚██╗
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝

░█████╗░░█████╗░██╗░░░░░██╗░░░░░
██╔══██╗██╔══██╗██║░░░░░██║░░░░░
██║░░╚═╝███████║██║░░░░░██║░░░░░
██║░░██╗██╔══██║██║░░░░░██║░░░░░
╚█████╔╝██║░░██║███████╗███████╗
░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝
            """)
        
        print(f"{Fore.RED}{Style.BRIGHT}⚡ {Fore.WHITE}Geliştirici: {Fore.CYAN}Vornexx ")
        print(f"{Fore.RED}{Style.BRIGHT}⚡ {Fore.GREEN}Github : VornexxBaba {Fore.CYAN} Instagram : mr.vornexx")
        print(f"{Fore.RED}{Style.BRIGHT}⚡ {Fore.WHITE}Tarih: {Fore.CYAN}{datetime.now().strftime('%d.%m.%Y %H:%M')}")
        print(f"{Fore.RED}{Style.BRIGHT}⚡ {Fore.WHITE}Termux Uyumlu: {Fore.GREEN}✓")
        print(f"{Fore.RED}{Style.BRIGHT}{'─'*55}\n")

    def animasyonlu_yaz(self, metin, hiz=0.03, renk=None):
        if renk is None:
            renk = Fore.WHITE
        for harf in metin:
            sys.stdout.write(f"{renk}{harf}")
            sys.stdout.flush()
            time.sleep(hiz)
        print()
    
    def durum_goster(self, baslik, durum, detay=""):
        simgeler = {
            'basari': f"{Fore.GREEN}✅",
            'hata': f"{Fore.RED}❌",
            'bilgi': f"{Fore.CYAN}ℹ️",
            'uyari': f"{Fore.YELLOW}⚠️",
            'calisiyor': f"{Fore.BLUE}🔄"
        }
        
        simge = simgeler.get(durum, "•")
        
        if durum == 'basari':
            renk = Fore.GREEN
        elif durum == 'hata':
            renk = Fore.RED
        elif durum == 'uyari':
            renk = Fore.YELLOW
        elif durum == 'bilgi':
            renk = Fore.CYAN
        elif durum == 'calisiyor':
            renk = Fore.BLUE
        else:
            renk = Fore.WHITE
            
        print(f"{simge} {Fore.WHITE}{baslik}: {renk}{detay}")
    
    def menu_goster(self):
        menu = f"""
{Fore.CYAN}{Style.BRIGHT}╔══════════════════════════════════════════════════╗
║                                                      ║
║  {Fore.YELLOW}[1] {Fore.WHITE}Tekli Arama Başlat                            ║
║  {Fore.YELLOW}[2] {Fore.WHITE}Çoklu Arama Başlat (Liste)                     ║
║  {Fore.YELLOW}[3] {Fore.WHITE}Ayarları Değiştir                              ║
║  {Fore.YELLOW}[4] {Fore.WHITE}İstatistikleri Göster                          ║
║  {Fore.YELLOW}[5] {Fore.WHITE}Çıkış                                         ║
║                                                      ║
{Fore.CYAN}╚══════════════════════════════════════════════════╝
        """
        print(menu)

class RateLimiter:
    
    def __init__(self, bekleme_suresi=300):
        self.bekleme_suresi = float(bekleme_suresi)
        self.cagri_kayitlari = {}
        self.lock = Lock()
        self.istatistikler = defaultdict(int)
    
    def kontrol_et(self, numara):
        suanki_zaman = time.time()
        
        with self.lock:
            son_arama = self.cagri_kayitlari.get(numara)
            
            if son_arama is None or (suanki_zaman - son_arama) >= self.bekleme_suresi:
                self.cagri_kayitlari[numara] = suanki_zaman
                self.istatistikler['izin_verilen'] += 1
                return True
            else:
                kalan_sure = self.bekleme_suresi - (suanki_zaman - son_arama)
                self.istatistikler['reddedilen'] += 1
                return False, kalan_sure
    
    def bekleme_suresi_degistir(self, yeni_sure):
        self.bekleme_suresi = float(yeni_sure)
        
    def istatistik_al(self):
        return dict(self.istatistikler)

class TelzIstemciGelismis:
    
    TEMEL_URL = "https://api.telz.com/"
    BASLIKLAR = {
        'User-Agent': "Telz-Android/17.5.33",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json; charset=UTF-8"
    }
    
    def __init__(self, android_id=None, app_version="17.5.33", os="android", os_version="15"):
        self.android_id = android_id or self._rastgele_android_id()
        self.app_version = app_version
        self.os = os
        self.os_version = os_version
        self.uuid = str(uuid.uuid4())
        self.session = requests.Session()
        self.session.headers.update(self.BASLIKLAR)
        
        self.istatistikler = {
            'toplam_istek': 0,
            'basarili_istek': 0,
            'basarisiz_istek': 0,
            'son_hata': None
        }
    
    @staticmethod
    def _rastgele_android_id():
        return uuid.uuid4().hex[:16]
    
    @staticmethod
    def _rastgele_cihaz_adi():
        markalar = ["Pixel", "Xiaomi", "Samsung", "OnePlus", "Moto", "Realme", "Oppo"]
        modeller = ["Pro", "Ultra", "Lite", "Max", "Plus", "5G"]
        return f"{random.choice(markalar)} {random.choice(modeller)}-{uuid.uuid4().hex[:6]}"
    
    def _api_istegi(self, endpoint, veri, timeout=15, tekrar_sayisi=2):
        url = self.TEMEL_URL + endpoint
        istek_verisi = veri.copy()
        
        istek_verisi.update({
            "android_id": self.android_id,
            "app_version": self.app_version,
            "os": self.os,
            "os_version": self.os_version,
            "ts": int(time.time() * 1000),
            "uuid": self.uuid
        })
        
        for deneme in range(tekrar_sayisi):
            try:
                self.istatistikler['toplam_istek'] += 1
                yanit = self.session.post(
                    url,
                    data=json.dumps(istek_verisi),
                    timeout=timeout
                )
                
                if yanit.status_code == 429:
                    retry_after = yanit.headers.get("Retry-After", "?")
                    raise RuntimeError(
                        f"Hız limiti aşıldı! {retry_after} saniye sonra tekrar deneyin."
                    )
                
                yanit.raise_for_status()
                self.istatistikler['basarili_istek'] += 1
                
                try:
                    return yanit.json()
                except ValueError:
                    return yanit.text
                    
            except Exception as e:
                self.istatistikler['basarisiz_istek'] += 1
                self.istatistikler['son_hata'] = str(e)
                
                if deneme < tekrar_sayisi - 1:
                    time.sleep(2 ** deneme)
                    continue
                raise
    
    def kimlik_listesi_al(self):
        return self._api_istegi("app/auth_list", {"event": "auth_list"})
    
    def cihaz_calistir(self, cihaz_adi=None, ipv4="10.1.10.1", ipv6="FE80::1", dil="tr"):
        cihaz_adi = cihaz_adi or self._rastgele_cihaz_adi()
        return self._api_istegi("app/run", {
            "event": "run",
            "device_name": cihaz_adi,
            "ipv4_address": ipv4,
            "ipv6_address": ipv6,
            "lang": dil,
            "network_country": "tr",
            "network_type": "4G",
            "roaming": "no",
            "root": "no",
            "run_id": "",
            "sim_country": "tr"
        })
    
    def buton_durumu_kontrol(self, buton="on_reg_continue"):
        return self._api_istegi("app/stat_btns", {
            "event": "stat_btns",
            "btn": buton
        })
    
    def numara_dogrula(self, telefon, bolge="TR"):
        return self._api_istegi("app/validate_phonenumber", {
            "event": "validate_phonenumber",
            "phone": telefon,
            "region": bolge
        })
    
    def arama_baslat(self, telefon, deneme="0", dil="tr"):
        return self._api_istegi("app/auth_call", {
            "event": "auth_call",
            "phone": telefon,
            "attempt": deneme,
            "lang": dil
        })
    
    def arama_cevapla(self, telefon, basarili=True):
        return self._api_istegi("app/auth_call_response", {
            "event": "auth_call_response",
            "phone": telefon,
            "success": bool(basarili)
        })

class AramaMotoru:
    
    def __init__(self):
        self.ui = AnimasyonluArayuz()
        self.rate_limiter = RateLimiter(bekleme_suresi=300)
        self.mod = "NORMAL"
        self.hedef_numaralar = []
        self.aktif = True
        self.genel_istatistikler = {
            'toplam_arama': 0,
            'basarili_arama': 0,
            'basarisiz_arama': 0,
            'baslangic_zamani': datetime.now(),
            'api_istekleri': 0
        }
        self.ayarlar = {
            'bekleme_suresi': 300,
            'animasyon_hizi': 0.03,
            'otomatik_cevap': True,
            'debug_modu': False,
            'maksimum_tekrar': 3
        }
    
    def baslat(self):
        try:
            self.ui.banner_goster()
            self.ui.animasyonlu_yaz("Sistem baslatiliyor...", 0.02, Fore.CYAN)
            
            self._bagimlilik_kontrol()
            
            while self.aktif:
                self.ui.menu_goster()
                secim = input(f"{Fore.YELLOW}Seciminiz (1-5): {Fore.WHITE}")
                
                if secim == "1":
                    self._tekli_arama()
                elif secim == "2":
                    self._coklu_arama()
                elif secim == "3":
                    self._ayarlar_menu()
                elif secim == "4":
                    self._istatistik_goster()
                elif secim == "5":
                    self._cikis()
                else:
                    print(f"{Fore.RED}Gecersiz secim!")
                    time.sleep(1)
                    
        except KeyboardInterrupt:
            self._cikis()
        except Exception as e:
            print(f"{Fore.RED}Beklenmeyen hata: {e}")
            if self.ayarlar['debug_modu']:
                import traceback
                traceback.print_exc()
            time.sleep(3)
    
    def _bagimlilik_kontrol(self):
        required = ['requests', 'colorama']
        missing = []
        
        for lib in required:
            try:
                __import__(lib)
            except ImportError:
                missing.append(lib)
        
        if missing:
            self.ui.durum_goster("Kutuphane", "uyari", f"Eksik: {', '.join(missing)}")
            print(f"{Fore.YELLOW}Yuklemek icin: pip install {' '.join(missing)}")
            time.sleep(2)
    
    def _tekli_arama(self):
        self.ui.banner_goster()
        
        print(f"\n{Fore.CYAN}{'─'*55}")
        numara = input(f"{Fore.WHITE}Hedef numara ({Fore.YELLOW}+90 ile baslayin{Fore.WHITE}): ").strip()
        
        if not numara:
            print(f"{Fore.RED}Numara bos olamaz!")
            time.sleep(1)
            return
            
        if not numara.startswith("+"):
            numara = "+90" + numara
        
        self.ui.animasyonlu_yaz(f"\nNumara dogrulaniyor: {numara}", 0.02, Fore.CYAN)
        
        istemci = TelzIstemciGelismis()
        self.genel_istatistikler['toplam_arama'] += 1
        
        adimlar = [
            ("Kimlik dogrulama", lambda: istemci.kimlik_listesi_al()),
            ("Cihaz hazirlama", lambda: istemci.cihaz_calistir()),
            ("Buton kontrolu", lambda: istemci.buton_durumu_kontrol()),
            ("Numara dogrulama", lambda: istemci.numara_dogrula(numara)),
        ]
        
        basarili_adimlar = 0
        for adim_adi, islem in adimlar:
            try:
                self.ui.yukleniyor_animasyonu(adim_adi, 1.5)
                sonuc = islem()
                self.ui.durum_goster(adim_adi, "basari", "Tamamlandi")
                basarili_adimlar += 1
                self.genel_istatistikler['api_istekleri'] += 1
            except Exception as e:
                self.ui.durum_goster(adim_adi, "hata", str(e)[:50])
                if self.ayarlar['debug_modu']:
                    import traceback
                    traceback.print_exc()
                return
        
        if basarili_adimlar == len(adimlar):
            try:
                print(f"\n{Fore.YELLOW}{'─'*55}")
                self.ui.animasyonlu_yaz("Arama baslatiliyor...", 0.03, Fore.GREEN)
                
                kontrol_sonucu = self.rate_limiter.kontrol_et(numara)
                if kontrol_sonucu == True or (isinstance(kontrol_sonucu, tuple) and kontrol_sonucu[0]):
                    for i in range(21):
                        yuzde = (i / 20) * 100
                        self.ui.ilerleme_cubugu(yuzde)
                        time.sleep(0.3)
                    print()
                    
                    sonuc = istemci.arama_baslat(numara)
                    self.genel_istatistikler['basarili_arama'] += 1
                    self.genel_istatistikler['api_istekleri'] += 1
                    
                    print(f"{Fore.GREEN}Arama basariyla baslatildi!")
                    
                    if self.ayarlar['debug_modu']:
                        print(f"{Fore.CYAN}Sunucu yaniti: {json.dumps(sonuc, indent=2)}")
                    
                    self.ui.animasyonlu_yaz("\n20 saniye bekleniyor...", 0.02, Fore.YELLOW)
                    for i in range(20, 0, -1):
                        sys.stdout.write(f"\r{Fore.CYAN}Kalan sure: {i} saniye ")
                        sys.stdout.flush()
                        time.sleep(1)
                    print()
                else:
                    kalan = kontrol_sonucu[1] if isinstance(kontrol_sonucu, tuple) else self.ayarlar['bekleme_suresi']
                    print(f"{Fore.RED}Bu numara icin {kalan:.0f} saniye beklemelisiniz!")
                    self.genel_istatistikler['basarisiz_arama'] += 1
                    
            except Exception as e:
                self.ui.durum_goster("Arama", "hata", str(e)[:50])
                self.genel_istatistikler['basarisiz_arama'] += 1
                if self.ayarlar['debug_modu']:
                    import traceback
                    traceback.print_exc()
        
        input(f"\n{Fore.CYAN}Devam etmek icin ENTER...")
    
    def _coklu_arama(self):
        self.ui.banner_goster()
        print(f"\n{Fore.CYAN}{'─'*55}")
        print(f"{Fore.YELLOW}Coklu Arama Modu")
        print(f"{Fore.CYAN}{'─'*55}")
        
        print(f"\n{Fore.WHITE}Numaralari alt alta girin (Cikmak icin bos satir):")
        print(f"{Fore.CYAN}Ornek: +905001234567")
        
        numaralar = []
        while True:
            numara = input(f"{Fore.GREEN}Numara {len(numaralar)+1}: {Fore.WHITE}").strip()
            if not numara:
                break
            if not numara.startswith("+"):
                numara = "+90" + numara
            numaralar.append(numara)
        
        if not numaralar:
            print(f"{Fore.RED}Hic numara girilmedi!")
            time.sleep(1)
            return
        
        print(f"\n{Fore.CYAN}Toplam {len(numaralar)} numara islenecek.")
        print(f"{Fore.YELLOW}Bu islem uzun surebilir!")
        
        onay = input(f"{Fore.WHITE}Devam etmek istiyor musunuz? (e/h): ").lower()
        if onay != 'e':
            return
        
        basarili = 0
        basarisiz = 0
        
        for i, numara in enumerate(numaralar, 1):
            print(f"\n{Fore.CYAN}{'─'*55}")
            print(f"{Fore.YELLOW}[{i}/{len(numaralar)}] Isleniyor: {numara}")
            
            try:
                istemci = TelzIstemciGelismis()
                
                istemci.kimlik_listesi_al()
                istemci.cihaz_calistir()
                istemci.buton_durumu_kontrol()
                istemci.numara_dogrula(numara)
                
                kontrol_sonucu = self.rate_limiter.kontrol_et(numara)
                if kontrol_sonucu == True or (isinstance(kontrol_sonucu, tuple) and kontrol_sonucu[0]):
                    istemci.arama_baslat(numara)
                    basarili += 1
                    self.ui.durum_goster("Sonuc", "basari", f"Arama baslatildi")
                else:
                    basarisiz += 1
                    kalan = kontrol_sonucu[1] if isinstance(kontrol_sonucu, tuple) else self.ayarlar['bekleme_suresi']
                    self.ui.durum_goster("Sonuc", "hata", f"Rate limit: {kalan:.0f}s")
                    
            except Exception as e:
                basarisiz += 1
                self.ui.durum_goster("Sonuc", "hata", str(e)[:50])
            
            if i < len(numaralar):
                time.sleep(5)
        
        print(f"\n{Fore.CYAN}{'─'*55}")
        print(f"{Fore.GREEN}Basarili: {basarili}")
        print(f"{Fore.RED}Basarisiz: {basarisiz}")
        
        self.genel_istatistikler['toplam_arama'] += basarili + basarisiz
        self.genel_istatistikler['basarili_arama'] += basarili
        self.genel_istatistikler['basarisiz_arama'] += basarisiz
        
        input(f"\n{Fore.CYAN}Devam etmek icin ENTER...")
    
    def _ayarlar_menu(self):
        while True:
            self.ui.banner_goster()
            print(f"{Fore.CYAN}{Style.BRIGHT}╔══════════════════════════════════════════════════╗")
            print(f"║                                                      ║")
            print(f"║  {Fore.YELLOW}[1] {Fore.WHITE}Bekleme Suresi: {Fore.GREEN}{self.ayarlar['bekleme_suresi']} saniye")
            print(f"║  {Fore.YELLOW}[2] {Fore.WHITE}Debug Modu: {Fore.GREEN}{self.ayarlar['debug_modu']}")
            print(f"║  {Fore.YELLOW}[3] {Fore.WHITE}Ana Menüye Dön                                    ║")
            print(f"║                                                      ║")
            print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝")
            
            secim = input(f"{Fore.YELLOW}Seçiminiz (1-3): {Fore.WHITE}").strip()
            if secim == "1":
                yeni_sure = input(f"{Fore.WHITE}Yeni bekleme süresi (sn): ").strip()
                if yeni_sure.isdigit():
                    self.ayarlar['bekleme_suresi'] = int(yeni_sure)
                    self.rate_limiter.bekleme_suresi_degistir(yeni_sure)
            elif secim == "2":
                self.ayarlar['debug_modu'] = not self.ayarlar['debug_modu']
            elif secim == "3":
                break

    def _istatistik_goster(self):
        self.ui.banner_goster()
        gecen_sure = datetime.now() - self.genel_istatistikler['baslangic_zamani']
        print(f"{Fore.CYAN}📊 Sistem İstatistikleri")
        print(f"{Fore.CYAN}{'─'*55}")
        print(f"{Fore.WHITE}Çalışma Süresi: {Fore.YELLOW}{gecen_sure.seconds} saniye")
        print(f"{Fore.WHITE}Toplam Arama: {Fore.YELLOW}{self.genel_istatistikler['toplam_arama']}")
        print(f"{Fore.WHITE}Başarılı Arama: {Fore.GREEN}{self.genel_istatistikler['basarili_arama']}")
        print(f"{Fore.WHITE}Başarısız Arama: {Fore.RED}{self.genel_istatistikler['basarisiz_arama']}")
        print(f"{Fore.WHITE}API İstekleri: {Fore.BLUE}{self.genel_istatistikler['api_istekleri']}")
        input(f"\n{Fore.CYAN}Devam etmek için ENTER...")

    def _cikis(self):
        self.ui.banner_goster()
        self.ui.animasyonlu_yaz("Sistemden çıkılıyor... Güle güle!", 0.03, Fore.MAGENTA)
        self.aktif = False
        sys.exit(0)

if __name__ == "__main__":
    motor = AramaMotoru()
    motor.baslat()                 