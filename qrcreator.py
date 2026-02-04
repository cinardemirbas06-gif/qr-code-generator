import qrcode

def qr_yap():
    print("-----QR KOD OLUŞTURUCUYA HOŞGELDİNİZ-----")

    veri = input("QR DÖNÜŞTÜRÜLCEK METİN GİRİN :")

    if not veri:
        print("BOŞ VERİ GİRDİNİZ")
        return

    dosya_adi = input("RESİM ADI NE OLSUN ? (ÖRN:BENİM SİTE)")
    if not dosya_adi.endswith(".png"):
        dosya_adi += ".png"


        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(veri)
        qr.make(fit=True)


        img = qr.make_image(fill_color="black", back_color="white")


        try:
            img.save(dosya_adi)

            print(f"\n✅ BAŞARILI! '{dosya_adi}' oluşturuldu.")
            print("Dosyanın olduğu klasöre bakabilirsin.")
        except Exception as e:
         print(f"Hata oluştu: {e}")


if __name__ == "__main__":
    qr_yap()