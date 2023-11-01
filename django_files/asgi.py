"""
ASGI config for django_files project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

"""


Acest fișier ASGI (Asynchronous Server Gateway Interface) este parte a configurării unei 
aplicații Django pentru a permite gestionarea cererilor asincrone. ASGI este o interfață 
care permite serverelor web să proceseze cereri asincrone în Django, ceea ce este util pentru 
aplicații care necesită gestionarea unui număr mare de conexiuni simultane sau cereri care pot 
dura mult timp.

"""


import os

from django.core.asgi import get_asgi_application


"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_files.settings'):

Acesta este un apel pentru a seta variabila de mediu DJANGO_SETTINGS_MODULE pentru a 
specifica modulul de setări Django care trebuie încărcat pentru această aplicație. În 
cazul de față, acesta este setat la "django_files.settings", ceea ce înseamnă că setările 
aplicației sunt citite din modulul "settings.py" din directorul "django_files".

"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_files.settings')


"""

application = get_asgi_application():

Această linie obține aplicația ASGI pentru gestionarea cererilor asincrone folosind funcția
get_asgi_application() din Django.

Aplicația ASGI este o componentă esențială a configurației pentru a permite gestionarea 
cererilor asincrone și asigurarea compatibilității cu serverele web și gateway-urile ASGI.

"""

application = get_asgi_application()

"""

În esență, acest fișier ASGI este utilizat pentru a configura aplicația Django astfel încât să 
poată gestiona cereri asincrone folosind ASGI. Când serverul web sau gateway-ul ASGI primește o 
cerere pentru aplicația Django, va utiliza această configurație ASGI pentru a direcționa cererea 
către aplicație și pentru a gestiona cererile asincrone în mod corespunzător.

"""