from time import sleep as bekle

def toplama():
    sayi1 = int(input("Toplanacak İlk Sayıyı Giriniz: "))
    sayi2 = int(input("Toplanacak İkinci Sayıyı Giriniz: "))
    print("Hesaplanıyor...")
    bekle(1)
    print("Toplam: " + str(sayi1+sayi2))
    bekle(1)
    soru = input("Ana Menüye Dönmek İçin(a) Mevcut İşleme Devam Etmek için(d) Yazınız: ")
    if soru == "a":
        main()
        return
    if soru == "d":
        toplama()
        return
    else:
        print("Lütfen Sadece a-d Yazınız Otomatik Ana Menüye Döndünüz!")
        bekle(1)
        main()
        return
def cikartma():
    sayi1 = int(input("Çıkarılacak Sayıyı Giriniz: "))
    sayi2 = int(input("Çıkarılan Sayıyı Giriniz: "))
    print("Hesaplanıyor...")
    bekle(1)
    print("Sonuç: " + str(sayi1-sayi2))
    bekle(1)
    soru = input("Ana Menüye Dönmek İçin(a) Mevcut İşleme Devam Etmek için(d) Yazınız: ")
    if soru == "a":
        main()
        return
    if soru == "d":
        cikartma()
        return
    else:
        print("Lütfen Sadece a-d Yazınız Otomatik Ana Menüye Döndünüz!")
        bekle(1)
        main()
        return

def carpma():
    sayi1 = int(input("Çarpılan Sayıyı Giriniz: "))
    sayi2 = int(input("Çarpılacak Sayıyı Giriniz: "))
    print("Hesaplanıyor...")
    bekle(1)
    print("Sonuç: " + str(sayi1*sayi2))
    bekle(1)
    soru = input("Ana Menüye Dönmek İçin(a) Mevcut İşleme Devam Etmek için(d) Yazınız: ")
    if soru == "a":
        main()
        return
    if soru == "d":
        carpma()
        return
    else:
        print("Lütfen Sadece a-d Yazınız Otomatik Ana Menüye Döndünüz!")
        bekle(1)
        main()
        return

def bölme():
    sayi1 = int(input("Bölünen Sayıyı Giriniz: "))
    sayi2 = int(input("Bölen Sayıyı Giriniz: "))
    print("Hesaplanıyor...")
    bekle(1)
    print("Sonuç: " + str(sayi1+sayi2))
    bekle(1)
    soru = input("Ana Menüye Dönmek İçin(a) Mevcut İşleme Devam Etmek için(d) Yazınız: ")
    if soru == "a":
        main()
        return
    if soru == "d":
        toplama()
        return
    else:
        print("Lütfen Sadece a-d Yazınız Otomatik Ana Menüye Döndünüz!")
        bekle(1)
        main()
        return

def kalan():
    sayi1 = int(input("Bölünen Sayıyı Giriniz: "))
    sayi2 = int(input("Bölen Sayıyı Giriniz: "))
    print("Hesaplanıyor...")
    bekle(1)
    print("Kalan: " + str(sayi1%sayi2))
    bekle(1)
    soru = input("Ana Menüye Dönmek İçin(a) Mevcut İşleme Devam Etmek için(d) Yazınız: ")
    if soru == "a":
        main()
        return
    if soru == "d":
        toplama()
        return
    else:
        print("Lütfen Sadece a-d Yazınız Otomatik Ana Menüye Döndünüz!")
        bekle(1)
        main()
        return

def tam():
    sayi1 = int(input("Bölünen Sayıyı Giriniz: "))
    sayi2 = int(input("Bölen Sayıyı Giriniz: "))
    print("Hesaplanıyor...")
    bekle(1)
    print("Sonuç: " + str(sayi1//sayi2))
    bekle(1)
    soru = input("Ana Menüye Dönmek İçin(a) Mevcut İşleme Devam Etmek için(d) Yazınız: ")
    if soru == "a":
        main()
        return
    if soru == "d":
        toplama()
        return
    else:
        print("Lütfen Sadece a-d Yazınız Otomatik Ana Menüye Döndünüz!")
        bekle(1)
        main()
        return

def üst():
    sayi1 = int(input("Taban Sayıyı Giriniz: "))
    sayi2 = int(input("Kuvvet Sayıyı Giriniz: "))
    print("Hesaplanıyor...")
    bekle(1)
    print("Sonuç: " + str(sayi1**sayi2))
    bekle(1)
    soru = input("Ana Menüye Dönmek İçin(a) Mevcut İşleme Devam Etmek için(d) Yazınız: ")
    if soru == "a":
        main()
        return
    if soru == "d":
        toplama()
        return
    else:
        print("Lütfen Sadece a-d Yazınız Otomatik Ana Menüye Döndünüz!")
        bekle(1)
        main()
        return

def ekstralar():
    print("VKİ = Ağırlık (Kg) / boyun metre cinsinden karesi")
    bekle(1)
    print("""
18, 5 kg/m.'nin altında olanlar: Zayıf
18.5 – 24, 9 kg/m. arasında olanlar: Normal kilolu
25 – 29, 9 kg/m. arasında olanlar: Fazla kilolu
30 – 39, 9 kg/m. arasında olanlar: Obez
40 kg/m.'nin üzerinde olanlar: İleri derecede obez (morbid obez)""")
    bekle(1)
    agirlik = float(input("Kilonuzu Giriniz: "))
    boy = float(input("Boyunuzu Giriniz(Metre Cinsinden): "))**2
    print("VKİ Hesaplanıyor...")
    bekle(2)
    indeks = agirlik/boy
    if indeks < 18.5:
        mevcut = "Zayıf"
    elif indeks >= 18.5 and indeks <= 24.999999:
        mevcut = "Normal Kilolu"
    elif indeks >= 25 and indeks <= 29.999999:
        mevcut = "Fazla Kilolu"
    elif indeks >= 30 and indeks <= 39.999999:
        mevcut = "Obez"
    elif indeks > 40:
        mevcut = "Morbid Obez"
    print(f"Vücut Kitle İndeksiniz : {mevcut}({indeks})")
    soru = input("Ana Menüye Dönmek İçin(a) Mevcut İşleme Devam Etmek için(d) Yazınız: ")
    if soru == "a":
        main()
        return
    if soru == "d":
        ekstralar()
        return
    else:
        print("Lütfen Sadece a-d Yazınız Otomatik Ana Menüye Döndünüz!")
        bekle(1)
        main()
        return


def main():
    print("""
1) Toplama
2) Çıkartma
3) Çarpma
4) Bölme
5) Kalan Alma
6) Tam Bölme
7) Üst Alma
8) ekstralar(İstediğinizi Anlamadım Ama Ekstralarda Birşeyler Denedim:))
9) Çıkış
""")
    try:
        secim = int(input("Lütfen Bir İşlem Seçiniz: "))
        if secim > 9 or secim < 1:
            print("Lütfen 1-9 Arasında Rakam Giriniz")
            main()
        elif secim == 1:
            toplama()
        elif secim == 2:
            cikartma()
        elif secim == 3:
            carpma()
        elif secim == 4:
            bölme()
        elif secim == 5:
            kalan()
        elif secim == 6:
            tam()
        elif secim == 7:
            üst()
        elif secim == 8:
            ekstralar()
        elif secim == 9:
            exit()
        
    except Exception as e:
        print(e)

main()
