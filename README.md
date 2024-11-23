Company Attendance Uygulaması

Bu proje, şirket çalışanlarının giriş/çıkış saatlerini takip etmek, izin taleplerini yönetmek ve yetkililere bildirim göndermek için geliştirilmiştir.

Gereksinimler

Python 3.10

Django

Django Rest Framework

PostgreSQL

Redis (Celery ve Channel Layer için)

Docker (isteğe bağlı)

Kurulum

Depoyu Klonlayın

git clone <repository_link>
cd company_attendance

Sanal Ortam Oluşturun

python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

Gereksinimleri Yükleyin

pip install -r requirements.txt

Veritabanını Ayarlayın
PostgreSQL'de bir veritabanı oluşturun ve settings.py dosyasındaki veritabanı ayarlarını güncelleyin.

Veritabanı Migrasyonları

python manage.py migrate

Süper Kullanıcı Oluşturun

python manage.py createsuperuser

Celery Çalıştırma

celery -A company_attendance worker --loglevel=info

Django Geliştirme Sunucusunu Başlatın

python manage.py runserver

Channels (WebSocket) İçin Redis Sunucusunu Başlatın

redis-server

Swagger Dokümantasyonu
Swagger dokümantasyonuna erişmek için tarayıcınızda şu URL'yi açın: http://127.0.0.1:8000/swagger/

Docker Kullanımı

Docker Görüntüsü Oluşturun ve Konteyneri Çalıştırın

docker build -t company_attendance .
docker run -p 8000:8000 company_attendance

Özellikler

Çalışan Giriş/Çıkış Takibi

Yıllık İzin Yönetimi

Geç Kalma Bildirimleri

WebSocket ile Gerçek Zamanlı Bildirimler

Swagger ile API Dokümantasyonu
