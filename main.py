class Kullanici:
    def __init__(self,ad:str,hesapno:int,bakiye:int):
        self.ad = ad
        self.hesapno = hesapno
        self.bakiye = bakiye


hesaplar = []


class KullaniciYöneticisi:
    def __init__(self,hesap = False):
        self.hesap = hesap
        if self.hesap == False:
            self.hesap = False

        action = input("Bir işlem seçin. : ")
        if action == "":
            print("""
---------------------------
HATA! Bir işlem seçin.            

Yapılabilecek işlemler;
1 - Giriş
2 - Çıkış
3 - Para çek
4 - Para yatır
5 - Hesaplar
6 - Bilgilerim
7 - Hesap Aç
---------------------------""")

        if action == "1":
            if self.hesap != False:
                print("Zaten bi hesap açıkken giriş yapamazsınız.")
                KullaniciYöneticisi(self.hesap)
            self.giris()
        
    
        if action == "2":
            if self.hesap == False:
                print("Giriş yapmadan çıkış yapamazsınız.")
                KullaniciYöneticisi(False)

            self.cikis()
        
        if action == "3":
            if self.hesap == False:
                print("Giriş yapmadan para çekemezsiniz.")
                KullaniciYöneticisi(self.hesap)

            self.paraCek()

        if action == "4":
            if self.hesap == False:
                print("Giriş yapmadan para yatıramazsınız.")
                KullaniciYöneticisi(self.hesap)
            self.paraYatir()

        if action == "5":
            self.hesaplar()

        if action == "6":
            self.bilgilerim()
        
        if action == "7":
            self.hesapAc()


    def giris(self):
        kullanici_adi = input("Lütfen giriş yapmak istediğiniz kullanıcı adını belirtin.")

        try:
            hesap = next(item for item in hesaplar if item.ad == kullanici_adi)
            self.hesap = hesap
            print("Başarıyla giriş yaptınız.")
            KullaniciYöneticisi(hesap)
        except:
            print("Lütfen doğru kullanıcı adı girdiğinize emin olun.")
    
    def cikis(self):
        self.hesap = False
        KullaniciYöneticisi(False)
        return
    
    def paraCek(self):
        miktar = input("Çekmek istediğiniz para miktarını girin.")
        if miktar == "":
            print("Lütfen çekmek istediğiniz para miktarını girin.")
            self.paraCek()
        
        if int(miktar) > self.hesap.bakiye:
            print("Bakiyenizden fazlasını çekemezsiniz.")
            return self.paraCek()
        
        self.hesap.bakiye = self.hesap.bakiye - int(miktar)
        i = next((index for (index, d) in enumerate(hesaplar) if d.ad == self.hesap.ad), None)
        hesaplar[i] = self.hesap
        print(hesaplar[i].bakiye)
        KullaniciYöneticisi(self.hesap)

    def paraYatir(self):
        miktar = input("Yatırmak istediğiniz para miktarını girin.")
        if miktar == "":
            print("Lütfen yatırmak istediğiniz para miktarını girin.")
            self.paraYatir()
    
        self.hesap.bakiye = self.hesap.bakiye + int(miktar)
        i = next((index for (index, d) in enumerate(hesaplar) if d.ad == self.hesap.ad), None)
        hesaplar[i] = self.hesap
        print(f"{self.hesap.ad} hesabının yeni para miktarı {hesaplar[i].bakiye}")        
        KullaniciYöneticisi(self.hesap)

    def hesaplar(self):
        def filt(val):
            return val.ad
        print(list(map(filt,hesaplar)))
        KullaniciYöneticisi(self.hesap)


    def bilgilerim(self):
        if self.hesap == False:
            print("Giriş yapmadan hesap bilgilerinizi göremezsiniz.")
            return self.giris()
        
        print(f"Hesap adı : {self.hesap.ad}\nHesap Numarası: {self.hesap.hesapno}\nBakiye : {self.hesap.bakiye}")
        KullaniciYöneticisi(self.hesap)

    def hesapAc(self,ad="",hesapno=""):
        if ad == "":
            ad = input("Hesap adı : ")
            self.hesapAc(ad)
            return

        if hesapno == "":
            hesapno = input("Hesap no : ")
            self.hesapAc(ad,hesapno)
            return

        bakiye = input("Bakiye : ")

        if bakiye == "":
            self.hesapAc(ad,hesapno,bakiye)
            return
        bakiye = int(bakiye)
        
        hesap = Kullanici(ad,hesapno,bakiye)
        hesaplar.append(hesap)
        self.hesap = hesap
        print("Hesaba otomatik giriş yapıldı.")
        KullaniciYöneticisi(self.hesap)

        

while(True):
    KullaniciYöneticisi()