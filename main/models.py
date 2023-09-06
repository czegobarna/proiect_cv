"""

Acest fragment de cod reprezintă definirea unor modele de date în Django pentru o aplicație web.
Modelele sunt utilizate pentru a defini structura și comportamentul datelor din aplicație și pentru
a le stoca într-o bază de date.

"""

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

"""

Skill: Acest model definește abilitățile utilizatorului sau ale altor entități din aplicație.
Un skill are un nume (name), un scor (score), o imagine (image), și un indicator care indică 
dacă este o abilitate cheie (is_key_skill). Acest model poate fi folosit pentru a evidenția 
și a afișa abilitățile în profiluri sau în alte părți ale aplicației.

"""

class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

"""

UserProfile: Acest model reprezintă profilurile utilizatorilor. Un profil de utilizator 
este legat de modelul Django User prin intermediul unei relații OneToOneField. Acesta conține 
informații precum avatarul, titlul, biografia, abilitățile utilizatorului și un fișier CV. Acest 
model poate fi folosit pentru a gestiona detaliile personale ale utilizatorilor și pentru a le afișa pe paginile de profil.

"""

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

"""

ContactProfile: Acest model reprezintă profilurile de contact, care sunt utilizate pentru a 
stoca și a afișa mesajele de contact primite de la utilizatori. Acesta conține informații precum 
numele persoanei de contact, adresa de email și mesajul. Acest model poate fi folosit pentru a 
gestiona și a afișa mesajele de contact ale utilizatorilor.

"""

class ContactProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'

"""

Testimonial: Acest model reprezintă recomandările sau testimonialele primite de la utilizatori sau clienți. 
Acesta conține informații despre testimoniale, cum ar fi imaginea de reprezentare (thumbnail), numele persoanei, 
rolul, citatul și un indicator pentru a specifica dacă testimonialul este activ sau nu. Acest model poate 
fi folosit pentru a afișa testimoniale pe site-ul web.

"""

class Testimonial(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["name"]

    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


"""

Media: Acest model reprezintă fișiere media, cum ar fi imagini sau link-uri către alte resurse media.
Acesta conține informații despre fișiere media, cum ar fi imaginea sau URL-ul, numele și un indicator
care specifică dacă fișierul este o imagine sau nu. Acest model poate fi folosit pentru a gestiona și
a afișa resurse media în aplicație.

"""


class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]
	
    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

"""

Portfolio: Acest model reprezintă elementele de portofoliu, cum ar fi proiectele sau lucrările
efectuate de utilizator. Acesta conține informații despre proiecte, cum ar fi data, numele, 
descrierea, corpul textului, imaginea și un slug pentru URL-ul unic. Acest model poate fi folosit
pentru a afișa și a gestiona elemente de portofoliu.

"""

class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"

"""

Blog: Acest model reprezintă articolele de blog. Acesta conține informații despre articole, 
cum ar fi autorul, numele, descrierea, corpul textului, slug-ul pentru URL și imaginea. Acest 
model poate fi folosit pentru a gestiona și a afișa articole pe blog.

"""

class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

"""

Certificate: Acest model reprezintă certificatele sau diplomele obținute de utilizator sau de alte 
entități. Acesta conține informații despre certificate, cum ar fi data, numele, titlul și descrierea.
Acest model poate fi folosit pentru a gestiona și a afișa certificatele obținute.

"""

class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

"""

În ansamblu, aceste modele definesc structura datelor pentru diverse aspecte ale aplicației web 
Django și permit stocarea, gestionarea și afișarea acestor date într-o bază de date. Aceste date
pot fi apoi utilizate pentru a construi și a afișa pagini web, profiluri de utilizatori, 
testimoniale, portofolii, articole de blog și alte elemente ale aplicației tale.

"""