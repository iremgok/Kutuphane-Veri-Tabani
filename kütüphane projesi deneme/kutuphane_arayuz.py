import tkinter as tk
from tkinter.ttk import Combobox
from PIL import Image  # type: ignore


form = tk.Tk()
form.geometry('650x650+350+90')
form.config(bg='#ee82ee')
form.title('Kütüphanem')
root = tk.Frame(form)
root.pack()
metin = tk.Label(form, text='Kütüphane Arayüzüne Hoşgeldiniz!', fg='white', bg='#ee82ee', font='Times 14 bold')
metin.pack()


def gorsel():
    image_path = "C:\\Users\\irem\\OneDrive\\Masaüstü\\kütüphane projesi deneme\\ornek.jpg"
    image = Image.open(image_path)
    image.show()


def admin_giris():
    admin_isim_label = tk.Label(form, text='Admin Adınızı Giriniz:', fg='black', bg='pink', font='Times 10 bold')
    admin_isim_label.place(x=105, y=130)

    admin_isim_giris = tk.Entry(form)
    admin_isim_giris.place(x=250, y=130)

    admin_sifre_label = tk.Label(form, text='Admin Şifrenizi Giriniz:', fg='black', bg='pink', font='Times 10 bold')
    admin_sifre_label.place(x=105, y=160)

    admin_sifre_giris = tk.Entry(form, show='*') 
    admin_sifre_giris.place(x=250, y=160)


    def kontrol():
        admin_isim = admin_isim_giris.get()
        admin_sifre = admin_sifre_giris.get()

        if admin_isim == "irmm" and admin_sifre == "5555":
            takimlar = ['Kullanıcı Ekle', 'Kullanıcı Sil']
            kutu = Combobox(form, values=takimlar, textvariable=m)
            kutu.place(x=105, y=240)
            
            buton = tk.Button(form, text='Seç', command=yazdir)
            buton.place(x=105, y=270)
        else:
            hata_metni = tk.Label(form, text='Hatalı admin bilgileri, tekrar deneyiniz.', fg='white', bg='#ee82ee', font='Times 10 bold')
            hata_metni.place(x=105, y=240)

    giris_buton = tk.Button(form, text='Giriş', command=kontrol)
    giris_buton.place(x=105, y=190)



def kullanici_ekle():

    kullanici_isim_label = tk.Label(form, text='Yeni Kullanıcı Adınızı Giriniz:', fg='black', bg='pink', font='Times 10 bold')
    kullanici_isim_label.place(x=105, y=310)

    kullanici_isim_giris = tk.Entry(form)
    kullanici_isim_giris.place(x=300, y=310)

    kullanici_sifre_label = tk.Label(form, text='Yeni Kullanıcı Şifrenizi Giriniz:', fg='black', bg='pink', font='Times 10 bold')
    kullanici_sifre_label.place(x=105, y=340)

    kullanici_sifre_giris = tk.Entry(form, show='*')  
    kullanici_sifre_giris.place(x=300, y=340)

    def ekle():
        yeni_kullanici_isim = kullanici_isim_giris.get()
        yeni_kullanici_sifre = kullanici_sifre_giris.get()

        with open("kullanicilar.txt", "a") as f:
            f.write(yeni_kullanici_isim + "," + yeni_kullanici_sifre + "\n")

        basari_metni = tk.Label(form, text='Yeni kullanıcı başarıyla eklendi.', fg='white', bg='#ee82ee', font='Times 10 bold')
        basari_metni.place(x=105, y=410)

    giris_buton = tk.Button(form, text='Kaydet', command=ekle)
    giris_buton.place(x=105, y=375)



def kullanici_sil():
    def sil():
        silinecek_kullanici_isim = kullanici_isim_sil_giris.get()
        silinecek_kullanici_sifre = kullanici_sifre_sil_giris.get()

        with open("kullanicilar.txt", "r") as f:
            lines = f.readlines()

        with open("kullanicilar.txt", "w") as f:
            kullanici_bulundu = False
            for line in lines:
                kullanici_bilgileri = line.strip().split(",")
                if len(kullanici_bilgileri) == 2:  
                    dosya_kullanici_isim, dosya_kullanici_sifre = kullanici_bilgileri
                    if dosya_kullanici_isim != silinecek_kullanici_isim or dosya_kullanici_sifre != silinecek_kullanici_sifre:
                        f.write(line)
                    else:
                        kullanici_bulundu = True

        if kullanici_bulundu:
            metin.config(text='Kullanıcı başarıyla silindi.', fg='white', bg='#ee82ee')
        else:
            metin.config(text='Kullanıcı bulunamadı.', fg='white', bg='#ee82ee')

    kullanici_isim_sil_label = tk.Label(form, text='Silmek istediğiniz Kullanıcının Adınızı Giriniz:', fg='black', bg='pink', font='Times 10 bold')
    kullanici_isim_sil_label.place(x=105, y=310)

    kullanici_isim_sil_giris = tk.Entry(form)
    kullanici_isim_sil_giris.place(x=400, y=310)

    kullanici_sifre_sil_label = tk.Label(form, text='Silmek istediğiniz Kullanıcının Şifrenizi Giriniz:', fg='black', bg='pink', font='Times 10 bold')
    kullanici_sifre_sil_label.place(x=105, y=340)

    kullanici_sifre_sil_giris = tk.Entry(form, show='*')  
    kullanici_sifre_sil_giris.place(x=400, y=340)

    giris_buton = tk.Button(form, text='Sil', command=sil)
    giris_buton.place(x=105, y=375)

    metin = tk.Label(form, text='', fg='white', bg='#ee82ee', font='Times 10 bold')
    metin.place(x=105, y=410)



def kullanici():
    with open("kullanicilar.txt", "r") as f2:
        kullanici_bilgileri = [line.strip().split(",") for line in f2 if line.strip()]

        kullanici_isim_label = tk.Label(form, text='Kullanıcı Adınızı Giriniz:', fg='black', bg='pink', font='Times 10 bold')
        kullanici_isim_label.place(x=105, y=130)

        kullanici_isim_giris = tk.Entry(form)
        kullanici_isim_giris.place(x=265, y=130)

        kullanici_sifre_label = tk.Label(form, text='Kullanıcı Şifrenizi Giriniz:', fg='black', bg='pink', font='Times 10 bold')
        kullanici_sifre_label.place(x=105, y=160)

        kullanici_sifre_giris = tk.Entry(form, show='*')  
        kullanici_sifre_giris.place(x=265, y=160)


        def giris_kontrol():
            girilen_isim = kullanici_isim_giris.get()
            girilen_sifre = kullanici_sifre_giris.get()

            for dosya_kullanici_bilgisi in kullanici_bilgileri:
                if len(dosya_kullanici_bilgisi) == 2:
                    dosya_kullanici_isim, dosya_kullanici_sifre = dosya_kullanici_bilgisi
                    if girilen_isim == dosya_kullanici_isim and girilen_sifre == dosya_kullanici_sifre:
                        metin = tk.Label(form, text='Bilgileriniz Eşleşmiştir', fg='white', bg='#ee82ee', font='Times 10 bold')
                        metin.place(x=105, y=220)
                        takim = ['Kitap Bul', 'Kitap Ekle', 'Kitap Sil', 'Kitap Kirala', 'Kitap Geri Bırak']
                        kutu = Combobox(form, values=takim, textvariable=l)
                        kutu.place(x=105, y= 260)

                        buton1 = tk.Button(form, text='Seç', command=yazdir)
                        buton1.place(x=105, y=290)
                        return  
            metin = tk.Label(form, text='Kullanıcı adı veya şifresi yanlıştır. Tekrar deneyiniz.', fg='white', bg='#ee82ee', font='Times 10 bold')
            metin.place(x=105, y=220)

        giris_buton = tk.Button(form, text='Giriş', command=giris_kontrol)
        giris_buton.place(x=105, y=190)


def kitap_bul():

    isbn_no_label = tk.Label(form, text='Sorgulamak istediğiniz Kitabın ISBN no Giriniz:', fg='white', bg='blue', font='Times 10 bold')
    isbn_no_label.place(x=105, y=330)

    girilen_isbn = tk.Entry(form)
    girilen_isbn.place(x=400, y=330)

    def bul():
        girilen_isbn_no = girilen_isbn.get()

        with open("kitaplar.txt", "r") as f1:
            for line in f1:
                kitap_ozellikleri = line.strip().split(",")
                if girilen_isbn_no == kitap_ozellikleri[4]:
                    kitap_bilgisi = ", ".join(kitap_ozellikleri)
                    metin = tk.Label(form, text=kitap_bilgisi, fg='black', bg='#ee82ee', font='Times 10 bold')
                    metin.place(x=105, y=390)
                    return
            metin = tk.Label(form, text='Kitap Bulunamamıştır', fg='white', bg='#ee82ee', font='Times 10 bold')
            metin.place(x=105, y=390)

    bul_button = tk.Button(form, text="Kitabı Bul", command=bul)
    bul_button.place(x=105, y=360)


def kitap_ekle():

    kitap_bilgileri_label = tk.Label(form, text='Eklenecek kitabın ismi, yazarı, yayın yılı, yayın evi, ISBN, adet ve durumunu giriniz (virgülle ayırarak):', fg='white', bg='blue', font='Times 10 bold')
    kitap_bilgileri_label.place(x=105, y=330)

    kitap_bilgileri_giris = tk.Entry(form)
    kitap_bilgileri_giris.place(x=700, y=330)

    def kitap_bilgilerini_kaydet():
        kitap_bilgileri = kitap_bilgileri_giris.get()
        with open("kitaplar.txt", "a") as f1:
            f1.write(kitap_bilgileri + "\n")
        metin1 = tk.Label(form, text='Kitap Dosyaya Kaydedilmiştir', fg='white', bg='#ee82ee', font='Times 10 bold')
        metin1.place(x=105, y=395)

    kaydet_buton = tk.Button(form, text='Kaydet', command=kitap_bilgilerini_kaydet)
    kaydet_buton.place(x=105, y=360)



def kitap_sil():
    kitap_bilgileri_label = tk.Label(form, text='Silmek istediğiniz kitabın ISBN numarasını giriniz:', fg='white', bg='blue', font='Times 10 bold')
    kitap_bilgileri_label.place(x=105, y=330)

    kitap_bilgileri_giris = tk.Entry(form)
    kitap_bilgileri_giris.place(x=410, y=330)

    with open("kitaplar.txt", "r") as f1:
        satirlar = f1.readlines()
    
    def kitap_bilgileri_sil():
        kitap_bulundu = False
        with open("kitaplar.txt", "w") as f2:
            for satir in satirlar:
                kitap_ozellikleri = satir.strip().split(",")
                if kitap_bilgileri_giris.get() == kitap_ozellikleri[4]:
                    kitap_bulundu = True
                else:
                    f2.write(satir)

        if kitap_bulundu:
            metin1 = tk.Label(form, text='Kitap Başarıyla Silindi', fg='white', bg='#ee82ee', font='Times 10 bold')
            metin1.place(x=105, y=395)
        else:
            metin1 = tk.Label(form, text='Kitap Bulunamadı', fg='white', bg='#ee82ee', font='Times 10 bold')
            metin1.place(x=105, y=395)

    kaydet_buton = tk.Button(form, text='Sil', command=kitap_bilgileri_sil)
    kaydet_buton.place(x=105, y=360)




def kitap_kiralama():

    kitap_bilgileri_label = tk.Label(form, text='Kiralamak istediğiniz kitabın ISBN numarasını giriniz:', fg='white', bg='blue', font='Times 10 bold')
    kitap_bilgileri_label.place(x=105, y=330)

    kitap_bilgileri_giris = tk.Entry(form)
    kitap_bilgileri_giris.place(x=430, y=330)

    def kitap_bilgileri_kiralama():
        kitap_bulundu = False

        with open("kitaplar.txt", "r") as f1, open("kiralik.txt", "a+") as f4:
            lines = f4.readlines()
            f4.seek(0)
            for line in lines:
                kitap_ozellikleri = line.strip().split(",")
                if kitap_bilgileri_giris.get() == kitap_ozellikleri[4]:
                    kitap_ozellikleri[5] = str(int(kitap_ozellikleri[5]) - 1)
                    f4.write(",".join(kitap_ozellikleri) + "\n")
                    metin1 = tk.Label(form, text='Kitap Başarıyla Kiralandı', fg='white', bg='#ee82ee', font='Times 14 bold')
                    metin1.place(x=105, y=395)
                    kitap_bulundu = True
                    break

            if not kitap_bulundu:
                for line in f1:
                    kitap_ozellikleri = line.strip().split(",")
                    if kitap_bilgileri_giris.get() == kitap_ozellikleri[4]:
                        if int(kitap_ozellikleri[5]) > 1:
                            kitap_ozellikleri[5] = str(int(kitap_ozellikleri[5]) - 1)
                            kitap_ozellikleri[6] = "kiralik"
                            f4.write(",".join(kitap_ozellikleri) + "\n")
                            metin1 = tk.Label(form, text='Kitap Başarıyla Kiralandı', fg='white', bg='#ee82ee', font='Times 14 bold')
                            metin1.place(x=105, y=395)
                            kitap_bulundu = True
                            break
                        elif kitap_ozellikleri[5] == "1":
                            kitap_ozellikleri[6] = "kiralik"
                            f4.write(",".join(kitap_ozellikleri) + "\n")
                            metin1 = tk.Label(form, text='Kitap Başarıyla Kiralandı', fg='white', bg='#ee82ee', font='Times 14 bold')
                            metin1.place(x=105, y=395)
                            kitap_bulundu = True
                            break

                if not kitap_bulundu:
                    metin1 = tk.Label(form, text='Kitap Bulunamadı', fg='white', bg='#ee82ee', font='Times 14 bold')
                    metin1.place(x=105, y=395)
                    return 

            f1.seek(0)
            updated_lines = []
            for line in f1:
                kitap_ozellikleri = line.strip().split(",")
                if kitap_bilgileri_giris.get() == kitap_ozellikleri[4]:
                    kitap_ozellikleri[5] = str(int(kitap_ozellikleri[5]) - 1)
                updated_lines.append(",".join(kitap_ozellikleri) + "\n")

            f1.seek(0)
            f1.truncate()
            f1.writelines(updated_lines)
    
    kaydet_buton = tk.Button(form, text='Kirala', command=kitap_bilgileri_kiralama)
    kaydet_buton.place(x=105, y=360)



def kitap_geri_verme():

    kitap_bilgileri_label = tk.Label(form, text='Geri vermek istediğiniz kitabın ISBN numarasını giriniz:', fg='white', bg='blue', font='Times 10 bold')
    kitap_bilgileri_label.place(x=105, y=330)

    kitap_bilgileri_giris = tk.Entry(form)
    kitap_bilgileri_giris.place(x=450, y=330)

    def geri_birak():
        kitap_bulundu = False

        with open("kiralik.txt", "r") as f1:
            satirlar = f1.readlines()

        with open("kiralik.txt", "w") as f2:
            for satir in satirlar:
                kitap_ozellikleri = satir.strip().split(",")
                if kitap_bilgileri_giris.get() == kitap_ozellikleri[4]:
                    kitap_bulundu = True
                    metin1 = tk.Label(form, text='Kitap Başarıyla Geri Verildi', fg='white', bg='#ee82ee', font='Times 10 bold')
                    metin1.place(x=105, y=395)
                else:
                    f2.write(satir)

        if not kitap_bulundu:
            metin1 = tk.Label(form, text='Kitap Bulunamadı', fg='white', bg='#ee82ee', font='Times 10 bold')
            metin1.place(x=105, y=395)

    kaydet_buton = tk.Button(form, text='Geri Bırak', command=geri_birak)
    kaydet_buton.place(x=105, y=360)



m = tk.StringVar() 
k = tk.StringVar()
l = tk.StringVar()

def yazdir():

    secilen = k.get()
    secilen1 = m.get()
    secilen2 = l.get()

    if secilen == "Admin Girişi":
        admin_giris()
        if secilen1 == "Kullanıcı Ekle":        
            kullanici_ekle()
        elif secilen1 == "Kullanıcı Sil":
            kullanici_sil()
    elif secilen == "Kullanıcı Girişi":
        kullanici()
        if secilen2 == "Kitap Bul":
            kitap_bul()
        elif secilen2 == "Kitap Ekle":
            kitap_ekle()
        elif secilen2 == "Kitap Sil":
            kitap_sil()
        elif secilen2 == "Kitap Kirala":
            kitap_kiralama()
        elif secilen2 == "Kitap Geri Bırak":
            kitap_geri_verme()
    elif secilen == "Harita Göster":
        gorsel()


takimlar = ['Admin Girişi', 'Kullanıcı Girişi', 'Harita Göster']
kutu = Combobox(form, values=takimlar, textvariable=k)
kutu.place(x=105, y= 60)

buton = tk.Button(form, text='Seç', command=yazdir)
buton.place(x=105, y=90)


form.mainloop()