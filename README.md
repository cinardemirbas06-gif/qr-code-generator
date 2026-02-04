📱 Python QR Code Generator

Python ve qrcode kütüphanesi kullanılarak geliştirilmiş, metin, URL veya herhangi bir veriyi saniyeler içinde QR Koda dönüştüren ve .png formatında kaydeden pratik bir araçtır.

📌 Not: Projeyi çalıştırdıktan sonra oluşan QR kodun veya terminal çıktısının ekran görüntüsünü README’ye eklemeyi unutmayın.

🚀 Özellikler

⚡ Hızlı Dönüştürme
Girilen veriyi saniyeler içinde QR koda çevirir.

🎨 Özelleştirilebilir
QR kod dosya adını kullanıcı belirler.

🖨️ Yüksek Kalite Çıktı
Okunabilirliği yüksek ve standartlara uygun QR kod üretir.

🛡️ Hata Yönetimi
Boş veri girişine karşı korumalıdır.

🛠️ Kullanılan Teknolojiler

Python 3.x

qrcode
QR kod matrisini oluşturmak için.

Pillow (PIL)
Görüntü işleme ve .png formatında kaydetme işlemleri için.

💻 Kurulum ve Çalıştırma

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

1️⃣ Projeyi İndirin

Terminal veya Komut İstemi’ni (CMD) açın ve projeyi klonlayın
(ya da ZIP olarak indirip klasöre girin):

git clone (https://github.com/cinardemirbas06-gif/qr-code-generator/tree/main)

2️⃣ Gerekli Kütüphaneleri Yükleyin

Bu projenin çalışması için qrcode ve Pillow kütüphaneleri gereklidir:

pip install qrcode[pil]

3️⃣ Uygulamayı Başlatın
python qr_olusturucu.py

📝 Kullanım

Program çalıştığında sizden iki bilgi ister:

Veri
QR kodun içine gömülecek link veya metin

Dosya Adı
Oluşturulacak resmin bilgisayara hangi isimle kaydedileceği

📌 Örnek Terminal Çıktısı
--- QR KOD OLUŞTURUCU ---
QR Koda dönüştürülecek link veya metni girin: https://github.com/
Resim adı ne olsun? (örn: benim_site): github_qr

✅ BAŞARILI! 'github_qr.png' oluşturuldu.
Dosyanın olduğu klasöre bakabilirsin.

🖼️ Örnek Çıktı

📷 Buraya oluşturulan QR kodun ekran görüntüsünü ekleyebilirsiniz.
(Örn: screenshots/github_qr.png)

👨‍💻 Geliştirici

Geliştirici: Senin Adın
