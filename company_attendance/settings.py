import os
from pathlib import Path

# BASE_DIR ayarı
BASE_DIR = Path(__file__).resolve().parent.parent

# Gizli anahtar - Üretim ortamında bu değeri gizli tutun
SECRET_KEY = 'django-insecure-REPLACE_WITH_YOUR_SECRET_KEY'

# Geliştirme sırasında DEBUG ayarı
DEBUG = True

# İzin verilen hostlar
ALLOWED_HOSTS = ["127.0.0.1"]

# Yüklü Uygulamalar
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'drf_yasg',
    'channels',
    'employee',
    'manager',
]

# Middleware Ayarları
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Kök URL ayarları
ROOT_URLCONF = 'company_attendance.urls'

# Template Ayarları
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI ve ASGI Ayarları
WSGI_APPLICATION = 'company_attendance.wsgi.application'
ASGI_APPLICATION = 'company_attendance.routing.application'

# Veritabanı Ayarları
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Parola Doğrulama
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Uluslararasılaşma Ayarları
LANGUAGE_CODE = 'tr-tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Statik Dosyalar Ayarları
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Medya Dosyaları (isteğe bağlı)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Varsayılan birincil anahtar alanı türü
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django Rest Framework Ayarları
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

# Celery Ayarları (isteğe bağlı)
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

LOGOUT_REDIRECT_URL = '/'  # Çıkış yaptıktan sonra yönlendirilmesi gereken sayfa

# Şirket İş Başlangıç ve Bitiş Saatleri
WORK_START_TIME = '08:00'
WORK_END_TIME = '18:00'

# Tatil Günleri
HOLIDAYS = ['Cumartesi', 'Pazar']

# Yeni İşe Başlayan Personel İçin İzin Tanımlaması
NEW_EMPLOYEE_LEAVE_DAYS = 15
