"""
Django settings for django_files project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""


"""

Acesta este un fișier de configurare pentru un proiect Django, în care sunt definite diverse setări
și opțiuni pentru aplicația web. Iată o scurtă explicație a câtorva dintre cele mai importante elemente 
din acest fișier:

"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


"""

SECRET_KEY: Acesta este un secret crucial pentru securitatea aplicației Django.
Este utilizat pentru a proteja informațiile sensibile, cum ar fi parolele utilizatorilor
și sesiunile. Nu ar trebui niciodată dezvăluit public și trebuie să fie un șir foarte lung și complex.

"""

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e&p&dw*rxmk)o_e53(wxqwrxkqrn8s!$9t)2y56(1w#12$$zy2'


"""

DEBUG: Atunci când este setat pe True, această opțiune activează modul de depanare, 
ceea ce înseamnă că vei obține informații detaliate despre erorile din aplicație. 
Pentru producție, ar trebui să fie setat pe False pentru a ascunde aceste informații 
de erori publicului.

"""
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

"""

ALLOWED_HOSTS: Aici poți specifica o listă de nume de gazde (hostname-uri) 
care sunt permise să acceseze aplicația. Aceasta ajută la securizarea aplicației, 
limitând accesul doar la anumite domenii sau adrese IP.

"""


ALLOWED_HOSTS = []


# Application definition

"""

INSTALLED_APPS: Această listă enumeră toate aplicațiile Django instalate în proiect. 
Aici sunt enumerate aplicații precum 'django.contrib.admin' (pentru panoul de administrare Django), 
'main' (care probabil este propria aplicație personalizată) și 'ckeditor' (o aplicație pentru a lucra cu 
editorul HTML CKEditor).

"""

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'main',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_files.urls'


"""

TEMPLATES: Acesta definește configurația pentru șabloanele de afișare ale aplicației, inclusiv
modul în care sunt gestionate contextele și locațiile șabloanelor.

"""

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_files.context_processors.project_context'
            ],
        },
    },
]

WSGI_APPLICATION = 'django_files.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


"""

DATABASES: Aici sunt specificate setările pentru baza de date a aplicației. 
În acest caz, se folosește baza de date SQLite ca bază de date implicită.

"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


"""

STATICFILES_DIRS și STATIC_URL: Aceste setări permit gestionarea fișierelor statice precum CSS,
JavaScript și imagini. Acestea specifică directoarele în care se găsesc aceste fișiere și URL-ul 
de bază pentru a le accesa din șabloanele tale.

"""

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media')
]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"


"""

MEDIA_URL și MEDIA_ROOT: Asemănător cu fișierele statice, aceste setări permit gestionarea 
fișierelor media (de exemplu, imagini încărcate de utilizatori). MEDIA_URL specifică URL-ul 
pentru accesarea fișierelor media, iar MEDIA_ROOT specifică directorul în care aceste fișiere 
sunt stocate pe server.

"""

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

