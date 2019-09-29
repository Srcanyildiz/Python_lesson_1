benimAdim ="Sercan"
benimSoyadim = "Yıldız"

print(benimAdim)

sayi = 5
print("islem sonucu:",sayi)
print(benimAdim + " " + benimSoyadim)

full = benimAdim + " " + benimSoyadim
print("Kullanicinin adi soyadi:",full)

print("bige\nadam")
print ("""
bilge
adam
merhaba
sercan""")

metin = "\"Bilge Adam\" besiktas subesi \"Python\" dersleri\n"
print(metin * 2)

sayi1 = 50
sayi2 = 120
toplam = sayi1 + sayi2
print("Toplama işleminin sonucu: ",toplam)
print("Toplama işleminin sonucu: " + str(toplam))


# input("Lütfen adınızı giriniz: ")

sayi1 = int(input("Lütfen 1. sayiyi giriniz: "))
sayi2 = int(input("Lütfen 2. sayiyi giriniz: "))
toplama1 = sayi1+sayi2
cikartma = sayi1-sayi2
carpma = sayi1*sayi2
bolme = sayi1/sayi2
mod = sayi1%sayi2
ustel = sayi1**sayi2
print("Toplamı işleminin sonucu ", toplama1)
print("Çıkartma işleminin sonucu: ", cikartma)
print("Çarpma işleminin sonucu: ", carpma)
print("Bolme işleminin sonucu: ", round(bolme,2))
print("Mod işleminin sonucu: ", mod)
print("Üstel işleminin sonucu: ", ustel)


print("Toplamı işleminin sonucu " + str(toplama1) + '\n'
      + "Çıkartma işleminin sonucu: " + str(cikartma) + '\n'
      + "Bolme işleminin sonucu: ", str(round(bolme,2)) + '\n'
      + "Mod işleminin sonucu: " + str(mod) + '\n'
      + "Üstel işleminin sonucu: " + str(ustel))
