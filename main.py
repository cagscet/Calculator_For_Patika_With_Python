
print("Hesap Makinesi")
while True:
    Secim = input("Lütfen yapmak istediğiniz işlemi seçiniz (+,-,*,/): ")
    deger1 = float(input("İlk değeri giriniz : "))
    deger2 = float(input("İkinci değeri giriniz : "))

    result = 0
    if Secim == '+':
        result = deger1 + deger2
        print("Sonuç : ", result)
    elif Secim == '-':
        result = deger1 - deger2
        print("Sonuç : ", result)
    elif Secim == '*':
        result = deger1 * deger2
        print("Sonuç : ", result)
    elif Secim == '/':
        if deger2 != 0:  # Sıfıra bölme kontrolü
            result = deger1 / deger2
            print("Sonuç:", result)
        else:
            print("Hata: Bir sayı sıfıra bölünemez!")
    else:
        print("Geçersiz işlem seçimi! Lütfen tekrar deneyin.")
