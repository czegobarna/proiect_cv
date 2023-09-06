"""

Acest fragment de cod reprezintă un semnal (signal) în Django și o funcție de recepție (receiver) 
asociată acestui semnal. Semnalele în Django sunt utilizate pentru a gestiona evenimente sau acțiuni 
care au loc în cadrul aplicației și pentru a răspunde la aceste evenimente. În acest caz, semnalul 
este legat de modelul User al sistemului de autentificare Django, iar funcția de recepție este utilizată
pentru a crea un profil de utilizator (UserProfile) atunci când un nou utilizator este înregistrat în aplicație.

"""
# Iată cum funcționează acest fragment de cod:
# Importuri: Se importă modulele necesare pentru a lucra cu semnale și modelele aferente

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserProfile

"""

@receiver(post_save, sender=User): Aceasta este o decoratoare care înregistrează funcția 
create_profile ca o funcție de recepție pentru semnalul post_save asociat modelului User.
Semnalul post_save este declanșat atunci când un obiect User este salvat în baza de date, 
iar funcția create_profile va fi apelată după ce salvarea a fost efectuată cu succes.

"""

@receiver(post_save, sender=User)


# create_profile(sender, instance, created, **kwargs): Aceasta este funcția de recepție care este 
# apelată când semnalul post_save este declanșat. Parametrii funcției sunt:
# sender: Modelul care a declanșat semnalul (în acest caz, modelul User).
# instance: Instanța modelului care a fost salvată (în acest caz, instanța utilizatorului care tocmai a fost creat).
# created: Un indicator care indică dacă instanța a fost creată sau doar actualizată (în acest caz, verifică dacă un utilizator a fost creat sau doar actualizat).
# **kwargs: Argumente suplimentare.
# Funcția create_profile verifică dacă un nou utilizator a fost creat (created == True) și, în acest caz, creează un profil de utilizator asociat acestuia utilizând modelul UserProfile.

def create_profile(sender, instance, created, **kwargs):
	if created:
		userprofile = UserProfile.objects.create(user=instance)


""""

În ansamblu, acest fragment de cod asigură că atunci când un utilizator nou este înregistrat în
aplicație, un profil de utilizator corespunzător este creat automat pentru acel utilizator, astfel
încât să poți stoca și gestiona informații suplimentare despre utilizatori, cum ar fi avatarul, titlul, 
biografia și altele în modelul UserProfile

"""