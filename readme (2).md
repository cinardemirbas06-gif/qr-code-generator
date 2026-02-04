📱 Python QR Code Generator
Python ve qrcode kütüphanesi kullanılarak geliştirilmiş, metin URL veya herhangi bir veriyi saniyeler içinde QR Koda dönüştüren ve resim (.png) olarak kaydeden pratik bir araç.

(Not: Projeyi çalıştırıp oluşan QR kodun veya terminalin görüntüsünü buraya eklemeyi unutmayın!)

🚀 Özellikler
Hızlı Dönüştürme: Saniyeler içinde veriyi işler.

Özelleştirilebilir: Dosya adını kullanıcı belirler.

Yüksek Kalite: Okunabilirliği yüksek, standartlara uygun çıktı üretir.

Hata Yönetimi: Boş veri girişine karşı korumalıdır.

🛠️ Kullanılan Teknolojiler
Python 3.x

qrcode Kütüphanesi: QR kod matrisini oluşturmak için.

Pillow (PIL): Görüntü işleme ve kaydetme işlemleri için.

💻 Kurulum ve Çalıştırma
Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

1. Projeyi İndirin
Terminal veya Komut İstemi'ni (CMD) açın ve projeyi klonlayın (veya ZIP olarak indirin):

Bash
git clone https://github.com/KULLANICI_ADIN/qr-code-generator.git
cd qr-code-generator
2. Gerekli Kütüphaneyi Yükleyin
Bu projenin çalışması için qrcode ve görüntü işleme kütüphanesine ihtiyaç vardır:

Bash
pip install qrcode[pil]
3. Uygulamayı Başlatın
Bash
python qr_olusturucu.py
📝 Kullanım Örneği
Program çalıştığında sizden iki bilgi ister:

Veri: QR kodun içine gömülecek link veya yazı.

Dosya Adı: Resmin bilgisayara hangi isimle kaydedileceği.

Örnek Terminal Çıktısı:

Plaintext
--- QR KOD OLUŞTURUCU ---
QR Koda dönüştürülecek link veya metni girin: https://github.com/
Resim adı ne olsun? (örn: benim_site): github_qr

✅ BAŞARILI! 'github_qr.png' oluşturuldu.
Dosyanın olduğu klasöre bakabilirsin.
Geliştirici: [ÇINAR DEMİRBAŞ] 