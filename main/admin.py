"""

Acesta este un fragment de cod Python care face parte dintr-o aplicație Django și este destinat 
administrării conținutului site-ului sau aplicației web. Acest cod face uz de modulul Django admin
pentru a crea o interfață de administrare în care poți gestiona diferitele modele de date definite 
în aplicație. Iată o scurtă explicație a fiecărui model și a configurării sale:

"""

from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    Testimonial,
    Media,
    Portfolio,
    Blog,
    Certificate,
    Skill
    )

"""
UserProfileAdmin: Acesta este un model care reprezintă profilurile utilizatorilor. Cu ajutorul 
lui @admin.register(UserProfile), acest model este înregistrat în interfața de 
administrare. list_display specifică câmpurile afișate în lista de administrare.

"""

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

"""

ContactAdmin: Acest model, ContactProfile, pare a reprezenta detaliile de contact ale 
utilizatorilor sau ale altor entități. Acesta este înregistrat în administrație și afișează 
câmpurile timestamp și name

"""

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name',)

"""

TestimonialAdmin: Acest model, Testimonial, este înregistrat în administrație și afișează 
câmpurile name și is_active.

"""

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')

"""

MediaAdmin: Acest model, Media, pare a gestiona resurse media, cum ar fi imagini sau fișiere.
Acesta este înregistrat în administrație.

"""

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

"""

PortfolioAdmin și BlogAdmin: Aceste modele, Portfolio și Blog, gestionează elemente de portofoliu 
și blog. Acestea sunt înregistrate înadministrație și au câmpuri suplimentare, cum ar fi slug,
care sunt definite ca fiind readonly, ceea ce înseamnă că nu pot fi modificate direct din interfața
de administrare.

"""

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

"""

CertificateAdmin: Acest model, Certificate, gestionează certificatele. Acesta este înregistrat
în administrație și afișează câmpurile id și name.

"""

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name')

"""

SkillAdmin: Acest model, Skill, gestionează abilitățile utilizatorilor sau ale altor entități.
Acesta este înregistrat în administrație șiafișează câmpurile id, name și score.

"""

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score')

"""

În esență, această parte a codului Python face posibilă gestionarea și administrarea datelor din 
cadrul aplicației Django prin intermediul interfeței de administrare Django. Aceasta facilitează 
adăugarea, modificarea și ștergerea datelor într-un mod structurat și eficient.

"""