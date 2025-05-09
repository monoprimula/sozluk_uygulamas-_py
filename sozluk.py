import json
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)  # colorama'yı başlat

def ekrani_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def kelime_ekle(sozluk):
    kelime = input("Eklemek istediğiniz kelime: ").strip().lower()
    if kelime in sozluk:
        print(Fore.YELLOW + "Bu kelime zaten sözlükte var!")
        print(Fore.CYAN + f"Mevcut tanım: {sozluk[kelime]}")
        degistir = input("Tanımı değiştirmek ister misiniz? (e/h): ").lower()
        if degistir != 'e':
            return
    
    tanim = input("Kelimenin tanımını girin: ").strip()
    sozluk[kelime] = tanim
    print(Fore.GREEN + f"'{kelime}' kelimesi sözlüğe eklendi.")

def kelime_ara(sozluk):
    kelime = input("Aramak istediğiniz kelime: ").strip().lower()
    if kelime in sozluk:
        print(Fore.CYAN + f"{kelime}: {sozluk[kelime]}")
    else:
        print(Fore.RED + "Bu kelime sözlükte bulunamadı.")

def kelime_sil(sozluk):
    kelime = input("Silmek istediğiniz kelime: ").strip().lower()
    if kelime in sozluk:
        sil = input(Fore.YELLOW + f"'{kelime}' kelimesini silmek istediğinize emin misiniz? (e/h): ").lower()
        if sil == 'e':
            del sozluk[kelime]
            print(Fore.GREEN + f"'{kelime}' kelimesi silindi.")
    else:
        print(Fore.RED + "Bu kelime sözlükte bulunamadı.")

def kelime_duzenle(sozluk):
    kelime = input("Düzenlemek istediğiniz kelime: ").strip().lower()
    if kelime in sozluk:
        print(Fore.CYAN + f"Mevcut tanım: {sozluk[kelime]}")
        yeni_tanim = input("Yeni tanımı girin (boş bırakırsanız değişmez): ").strip()
        if yeni_tanim:
            sozluk[kelime] = yeni_tanim
            print(Fore.GREEN + "Tanım güncellendi.")
    else:
        print(Fore.RED + "Bu kelime sözlükte bulunamadı.")

def sozlugu_goruntule(sozluk):
    if not sozluk:
        print(Fore.YELLOW + "Sözlük boş.")
        return
    
    print(Fore.CYAN + "\n--- Sözlük İçeriği ---")
    for kelime, tanim in sorted(sozluk.items()):
        print(Fore.YELLOW + f"{kelime}: " + Fore.WHITE + f"{tanim}")
    print(Fore.CYAN + f"Toplam {len(sozluk)} kelime bulunuyor.")

def dosyaya_kaydet(sozluk, dosya_adi="sozluk.json"):
    try:
        with open(dosya_adi, 'w', encoding='utf-8') as dosya:
            json.dump(sozluk, dosya, ensure_ascii=False, indent=4)
        print(Fore.GREEN + f"Sözlük '{dosya_adi}' dosyasına kaydedildi.")
    except Exception as e:
        print(Fore.RED + f"Dosya kaydedilirken hata oluştu: {e}")

def dosyadan_yukle(dosya_adi="sozluk.json"):
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as dosya:
            sozluk = json.load(dosya)
        print(Fore.GREEN + f"Sözlük '{dosya_adi}' dosyasından yüklendi.")
        return sozluk
    except FileNotFoundError:
        print(Fore.YELLOW + "Dosya bulunamadı. Yeni bir sözlük oluşturuluyor.")
        return {}
    except Exception as e:
        print(Fore.RED + f"Dosya yüklenirken hata oluştu: {e}")
        return {}

def main():
    sozluk = {}
    ekrani_temizle()
    
    while True:
        print(Fore.YELLOW + "\n" + "="*30)
        print(Fore.CYAN + Back.BLACK + "   KENDİ SÖZLÜĞÜM   ")
        print(Fore.YELLOW + "="*30)
        print(Fore.GREEN + "1. Kelime Ekle")
        print(Fore.GREEN + "2. Kelime Ara")
        print(Fore.GREEN + "3. Kelime Sil")
        print(Fore.GREEN + "4. Kelime Düzenle")
        print(Fore.BLUE + "5. Tüm Sözlüğü Görüntüle")
        print(Fore.MAGENTA + "6. Sözlüğü Dosyaya Kaydet")
        print(Fore.MAGENTA + "7. Sözlüğü Dosyadan Yükle")
        print(Fore.RED + "8. Çıkış")
        
        secim = input(Fore.WHITE + "Seçiminiz (1-8): ")
        
        if secim == "1":
            kelime_ekle(sozluk)
        elif secim == "2":
            kelime_ara(sozluk)
        elif secim == "3":
            kelime_sil(sozluk)
        elif secim == "4":
            kelime_duzenle(sozluk)
        elif secim == "5":
            sozlugu_goruntule(sozluk)
        elif secim == "6":
            dosyaya_kaydet(sozluk)
        elif secim == "7":
            sozluk = dosyadan_yukle()
        elif secim == "8":
            print(Fore.YELLOW + "Program sonlandırılıyor...")
            break
        else:
            print(Fore.RED + "Geçersiz seçim! Lütfen 1-8 arasında bir sayı girin.")

if __name__ == "__main__":
    main()