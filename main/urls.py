"""

Acest fragment de cod reprezintă definirea rutelor URL (Uniform Resource Locator)pentru 
aplicația web Django. Rutele URL sunt utilizate pentru a determina cum sunt mapate adresele URL 
ale cererilor primite de la utilizatori la funcțiile și metodele corespunzătoare din aplicație. 
În acest caz, fragmentul de cod definește următoarele lucruri:

"""
# from django.urls import path: Se importă modulul path din Django, care este folosit pentru a defini rute URL pentru aplicație.

from django.urls import path
from . import views

"""

app_name = "main": Se definește un nume de aplicație pentru a evita conflicte de nume 
între diferite aplicații Django. Acest nume de aplicație este utilizat pentru a grupa 
rutele URL specifice acelei aplicații.

"""

app_name = "main"

"""

urlpatterns: Aici este definită o listă de rute URL și funcțiile corespunzătoare pe care 
trebuie să le fie asociate. Fiecare rută URL este definită folosind funcția path.

"""

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	]

"""

Aceste rute URL și vizualizările asociate permit navigarea și afișarea diferitelor pagini 
și conținut în cadrul aplicației web Django. Prin definirea acestor rute, poți gestiona modul
în care cererile utilizatorilor sunt procesate și afișate în aplicație.

"""