from pathlib import Path
import os


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# SECURITY
# =========================================================

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-development-secret-key-change-this"
)


# =========================================================
# DEBUG
# =========================================================
# Local:
#     DEBUG=True
#
# Khi deploy:
#     DEBUG=False
#
# Render sẽ đặt DEBUG=False bằng Environment Variable.

DEBUG = os.environ.get(
    "DEBUG",
    "True"
) == "True"


# =========================================================
# ALLOWED HOSTS
# =========================================================

ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost"
).split(",")


# =========================================================
# APPLICATIONS
# =========================================================

INSTALLED_APPS = [

    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # App của website
    "pizzaweb",
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise:
    # Cho phép Django phục vụ static files khi deploy
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================================================
# URL CONFIGURATION
# =========================================================

ROOT_URLCONF = "pizzashop.urls"


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [

    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "pizzaweb" / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =========================================================
# WSGI
# =========================================================

WSGI_APPLICATION = "pizzashop.wsgi.application"


# =========================================================
# DATABASE
# =========================================================
#
# Hiện tại vẫn dùng SQLite.
#
# Khi website deploy bản chính thức, có thể chuyển sang
# PostgreSQL sau.
#

DATABASES = {

    "default": {

        "ENGINE": "django.db.backends.sqlite3",

        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# =========================================================
# LANGUAGE / TIME ZONE
# =========================================================

LANGUAGE_CODE = "vi"

TIME_ZONE = "Asia/Ho_Chi_Minh"

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = "/static/"


# Thư mục static bạn đang dùng:
#
# D:\pizza 2\pizzashop\static\

STATICFILES_DIRS = [

    BASE_DIR / "static",
]


# Thư mục được tạo khi chạy:
#
# python manage.py collectstatic

STATIC_ROOT = BASE_DIR / "staticfiles"


# =========================================================
# WHITENOISE
# =========================================================
#
# Nén và lưu cache static files khi deploy.
#

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)


# =========================================================
# MEDIA FILES
# =========================================================
#
# Ảnh pizza upload từ Django Admin sẽ nằm ở:
#
# D:\pizza 2\pizzashop\media\pizza\
#

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================================================
# LOGIN / LOGOUT
# =========================================================

LOGIN_URL = "/login/"

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/login/"


# =========================================================
# CSRF
# =========================================================
#
# Local không cần thêm gì.
#
# Khi deploy HTTPS, thêm domain Render vào Environment Variable:
#
# CSRF_TRUSTED_ORIGINS=https://ten-web-cua-ban.onrender.com
#
# Sau này nếu dùng domain riêng:
#
# CSRF_TRUSTED_ORIGINS=https://pizzalinh.vn
#

CSRF_TRUSTED_ORIGINS = [

    origin.strip()

    for origin in os.environ.get(
        "CSRF_TRUSTED_ORIGINS",
        ""
    ).split(",")

    if origin.strip()
]


# =========================================================
# SESSION
# =========================================================

SESSION_COOKIE_AGE = 60 * 60 * 24 * 7