"""

Această configurație Django (MainConfig) face parte din aplicația ta Django (presupunând că 
aplicația ta se numește "main") și servește la configurarea comportamentului aplicației tale în 
cadrul framework-ului Django. În particular, această configurație are două funcții importante:

default_auto_field: Acesta este un câmp care specifică tipul implicit de câmp pentru chei primare
în modelele tale de bază. În acest caz, este setat la 'django.db.models.BigAutoField', ceea ce
înseamnă că atunci când definescți modelele în aplicația ta Django, cheile primare vor fi automat
de tipul BigAutoField, care este un câmp de tip întreg foarte mare și se generează automat. Poți
modifica acest comportament implicit pentru fiecare model în parte dacă este necesar.


name: Acest câmp specifică numele aplicației, în acest caz, "main". Este important pentru Django 
să știe cum să identifice aplicația ta în contextul întregului proiect Django.


ready(): Această metodă este utilizată pentru a efectua inițializări suplimentare sau configurări
în momentul încărcării aplicației. În acest caz, ea importă un modul numit "main.signals". Acest 
modul poate conține semnale personalizate sau funcții care să fie executate atunci când aplicația
este gata să ruleze. Semnalele sunt folosite în Django pentru a gestiona evenimente sau acțiuni 
în aplicație, cum ar fi atunci când un model este salvat sau actualizat. Acesta este un mod comun
de a extinde funcționalitatea aplicației Django și de a efectua operațiuni personalizate în răspuns 
la evenimente specifice.

În ansamblu, această configurație (MainConfig) oferă Django informațiile necesare pentru a 
gestiona corect aplicația ta și pentru a efectua operațiuni suplimentare în momentul încărcării 
aplicației.

"""

from django.apps import AppConfig



class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        import main.signals