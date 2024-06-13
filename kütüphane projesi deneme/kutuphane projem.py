from PIL import Image    # type: ignore

def gorsel():
    image_path = "C:\\Users\\irem\\OneDrive\\Masaüstü\\kütüphane projesi deneme\\ornek.jpg"
    image = Image.open(image_path)
    image.show()


class Admin:
    def __init__(self, ad, sifre):
        self.ad = ad
        self.sifre = sifre
    
    def admin_giris(self):
        while True:
            admin_isim = input("Admin adinizi giriniz: ")
            admin_sifre = input("Admin sifrenizi giriniz: ")
            with open("admin.txt", "r") as f3:
                for line in f3:
                    dosya_admin_isim, dosya_admin_sifre = line.strip().split(",")
                    if admin_isim == dosya_admin_isim and admin_sifre == dosya_admin_sifre:
                        print("Bilgileriniz eslesti.")
                        return  
                print("Admin adı veya şifresi yanlistir. Tekrar deneyiniz.")


    def kullanici_ekle(self):
        with open("kullanicilar.txt", "a") as f3:
            kullanici_adi = input("Kullanici adini giriniz: ")
            kullanici_sifresi = input("Kullanici sifresini giriniz: ")
            f3.write("\n" + kullanici_adi + "\n")
            f3.write(kullanici_sifresi)
            print("Kullanici bilgileri dosyaya kaydedildi.")


    def kullanici_sil(self):
        with open("kullanicilar.txt", "r+") as f3:
            satirlar = f3.readlines()

            silinecek_isim = input("Silmek istediginiz kullanicinin adini giriniz: ")
            silinecek_sifre = input("Silmek istediginiz kullanicinin sifresini giriniz: ")

            kullanici_bulundu = False
            f3.seek(0) 
            i = 0
            while i < len(satirlar):
                if satirlar[i].strip() == silinecek_isim and i + 1 < len(satirlar) and satirlar[i + 1].strip() == silinecek_sifre:
                    kullanici_bulundu = True
                    i += 2  
                else:
                    f3.write(satirlar[i])
                    i += 1

            f3.truncate()  
            if kullanici_bulundu:
                print("Kullanici basariyla silindi.")
            else:
                print("Bu isimde ve sifrede kullanici bulunamamistir. Tekrar deneyiniz.")


class Kitap:
    def __init__(self, isim, yazar, yayin_yili, yayin_evi, isbn, adet, durum):
        self.isim = isim
        self.yazar = yazar
        self.yayin_yili = yayin_yili
        self.yayin_evi = yayin_evi
        self.isbn = isbn
        self.adet = adet
        self.durum = durum

    def __str__(self):
        return f"{self.isim}, {self.yazar}, {self.yayin_yili}, {self.yayin_evi}, {self.isbn}, {self.adet}, {self.durum}"


def kitap_bul():
    isbn_no = input("Sorgulamak istediğiniz kitabın ISBN numarasını giriniz: ")
    with open("kitaplar.txt", "r") as f1:
        for line in f1:
            kitap_ozellikleri = line.strip().split(",")
            if isbn_no == kitap_ozellikleri[4]:
                return f"Kitap bulundu: {' - '.join(kitap_ozellikleri)}"
        return "Belirtilen ISBN numarasına sahip bir kitap bulunamadı."  


def kitap_ekle():
    with open("kitaplar.txt", "a") as f1:
        kitap_bilgileri = input("Eklenecek kitabin ismi, yazari, yayin_yili, yayın_evi, ISBN, adet ve durumunu giriniz (virgülle ayirarak): ")
        f1.write(kitap_bilgileri + "\n")
    print("Kitap dosyaya kaydedildi.")


def kitap_sil():
    with open("kitaplar.txt", "r") as f1:
        satirlar = f1.readlines()

    isbn_no = input("Silmek istediginiz kitabin ISBN numarasini giriniz: ")

    kitap_bulundu = False
    with open("kitaplar.txt", "w") as f2:
        for satir in satirlar:
            kitap_ozellikleri = satir.strip().split(",")
            if isbn_no == kitap_ozellikleri[4]:
                kitap_bulundu = True
            else:
                f2.write(satir)
    if kitap_bulundu:
        print("Kitap basariyla silindi.")
    else:
        print("Belirtilen ISBN numarasina sahip bir kitap bulunamadi.")


def kitap_kiralama():
    isbn_no = input("Kiralama yapmak istediğiniz kitabın ISBN numarasını giriniz: ")
    kitap_bulundu = False

    with open("kitaplar.txt", "r+") as f1, open("kiralik.txt", "a+") as f4:
        lines = f4.readlines()
        f4.seek(0)
        for line in lines:
            kitap_ozellikleri = line.strip().split(",")
            if isbn_no == kitap_ozellikleri[4]:
                kitap_ozellikleri[5] = str(int(kitap_ozellikleri[5]) - 1)
                f4.write(",".join(kitap_ozellikleri) + "\n")
                print("Kitap başarıyla kiralandı.")
                kitap_bulundu = True
                break

        if not kitap_bulundu:
            for line in f1:
                kitap_ozellikleri = line.strip().split(",")
                if isbn_no == kitap_ozellikleri[4]:
                    if int(kitap_ozellikleri[5]) > 1:
                        kitap_ozellikleri[5] = str(int(kitap_ozellikleri[5]) - 1)
                        kitap_ozellikleri[6] = "kiralik"
                        f4.write(",".join(kitap_ozellikleri) + "\n")
                        print("Kitap başarıyla kiralandı.")
                        kitap_bulundu = True
                        break
                    elif kitap_ozellikleri[5] == "1":
                        kitap_ozellikleri[6] = "kiralik"
                        f4.write(",".join(kitap_ozellikleri) + "\n")
                        print("Kitap başarıyla kiralandı.")
                        kitap_bulundu = True
                        break

            if not kitap_bulundu:
                print("Belirtilen ISBN numarasına sahip bir kitap bulunamadı.")
                return 

        f1.seek(0)
        updated_lines = []
        for line in f1:
            kitap_ozellikleri = line.strip().split(",")
            if isbn_no == kitap_ozellikleri[4]:
                kitap_ozellikleri[5] = str(int(kitap_ozellikleri[5]) - 1)
            updated_lines.append(",".join(kitap_ozellikleri) + "\n")

        f1.seek(0)
        f1.truncate()
        f1.writelines(updated_lines)

def kitap_geri_verme():
    isbn_no = input("Geri vermek istediğiniz kitabın ISBN numarasını giriniz: ")
    kitap_bulundu = False

    with open("kiralik.txt", "r") as f1:
        satirlar = f1.readlines()

    with open("kiralik.txt", "w") as f2:
        for satir in satirlar:
            kitap_ozellikleri = satir.strip().split(",")
            if isbn_no == kitap_ozellikleri[4]:
                kitap_bulundu = True
                print("Kitap başarıyla iade edildi.")
            else:
                f2.write(satir)

    if not kitap_bulundu:
        print("Belirtilen ISBN numarasına sahip bir kitap kiralık olarak bulunamadı.")


def kullanici():
    with open("kullanicilar.txt", "r") as f2:
        kullanici_bilgileri = f2.read().splitlines()
        while True:
            kullanici_isim = input("Kullanici adinizi giriniz: ")
            kullanici_sifre = input("Kullanici sifrenizi giriniz: ")
            if kullanici_isim in kullanici_bilgileri and kullanici_sifre in kullanici_bilgileri:
                print("Bilgileriniz eslesmistir.")
                break
            else:
                print("Kullanici adi veya sifresi yanlistir. Tekrar giriniz.")


def main():
    print("*KUTUPHANE ARAYUZUNE HOSGELDINIZ*")
    admin = Admin("admin_isim", "admin_sifre")
    while True:
        print("1- Admin Girisi")
        print("2- Kullanici Girisi")
        print("3- Kutuphane Haritasi")
        secenek = input("Yukaridaki Seceneklerden Birini Seciniz: ")
        if secenek == "1":
            admin.admin_giris()
            print("1- Kullanici Ekle")
            print("2- Kullanici Sil")
            secenek1 = input("Yukaridaki Seceneklerden Birini Seciniz: ")
            if secenek1 == "1":
                admin.kullanici_ekle()
            elif secenek1 == "2":
                admin.kullanici_sil()
            else:
                print("Yanlis Secenek Girdiniz. Tekrar Giriniz.")
        elif secenek == "2":
            kullanici()
            print("1- Kitap Bul")
            print("2- Kitap Ekle")
            print("3- Kitap Sil")
            print("4- Kitap Kirala")
            print("5- Kitap Geri Birak")
            secenek2 = input("Yukaridaki Seceneklerden Birini Seciniz: ")
            if secenek2 == "1":
                print(kitap_bul())
            elif secenek2 == "2":
                kitap_ekle()
            elif secenek2 == "3":
                kitap_sil()
            elif secenek2 == "4":
                kitap_kiralama()
            elif secenek2 == "5":
                kitap_geri_verme()
            else:
                print("Yanlis Secenek Girdiniz. Tekrar Giriniz.")
        elif secenek == "3":
            gorsel()
        else:
            print("Yanlis Secenek Girdiniz. Tekrar Giriniz.")


if __name__ == '__main__':
    main()

    #arayüz