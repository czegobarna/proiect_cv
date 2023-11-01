"""
resume_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""

Acest fișier reprezintă configurarea URL-urilor (rutele) pentru aplicația ta Django și este 
esențial pentru a direcționa cererile HTTP către view-urile corespunzătoare ale aplicației tale.

"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


"""

urlpatterns: Această listă conține toate rutele URL ale aplicației tale Django și indică către 
care view-uri trebuie să fie direcționate cererile HTTP. În exemplul tău, există două rute definite:

path('admin/', admin.site.urls): Această rută direcționează toate cererile care încep cu '/admin/' 
către panoul de administrare Django. Acesta este locul în care poți gestiona datele și configurările 
aplicației tale.

path('', include('main.urls', namespace="main")): Această rută direcționează cererile care nu se potrivesc
cu nicio altă rută către aplicația principală, care este definită în alt modul numit 'main.urls'. De asemenea,
un spațiu de nume (namespace) "main" este atribuit acestei aplicații, ceea ce permite gestionarea mai ușoară
a rutelor din aceasta.

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace="main")),
]

"""

Blocul if settings.DEBUG: Acest bloc de cod verifică dacă setarea DEBUG din fișierul de configurare 
Django (settings.py) este setată pe True. Dacă acesta este cazul, atunci se adaugă rute suplimentare 
pentru servirea fișierelor statice și a fișierelor media în timpul dezvoltării. Acest lucru este util 
pentru a putea vedea imediat schimbările în fișierele statice și media în timp ce dezvolți.


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT): Această linie adaugă o 
rută pentru servirea fișierelor statice (de exemplu, fișierele CSS și JavaScript) din directorul specificat 
în setările (STATIC_ROOT) la URL-ul specificat (STATIC_URL).


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT): Această linie adaugă o rută 
pentru servirea fișierelor media (de exemplu, imagini încărcate de utilizatori) din directorul specificat 
în setările (MEDIA_ROOT) la URL-ul specificat (MEDIA_URL).

"""

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""

Acest fișier de configurare pentru URL-uri asigură că cererile HTTP sunt corect direcționate 
către view-urile corespunzătoare în aplicația ta Django, facilitând astfel funcționarea 
corectă a site-ului web.

"""