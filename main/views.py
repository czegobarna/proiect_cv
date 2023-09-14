"""


Acest fragment de cod definește diverse vederi (views) în aplicația Django pentru gestionarea 
diferitelor pagini și funcționalități ale site-ului web. Iată o explicație detaliată a fiecărei
vederi și la ce se folosesc în program:

"""

from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate
	)

from django.views import generic


from . forms import ContactForm

"""

IndexView:

Această vedere este asociată cu pagina principală a site-ului web.
Template-ul utilizat pentru această vedere este "main/index.html".
Funcția get_context_data este folosită pentru a obține datele de context necesare pentru 
template-ul paginii principale. Aici se includ testimoniale,certificate, bloguri și portofoliu 
care sunt afișate pe pagina principală.

"""

class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True).order_by('-date')

		
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		return context


"""

ContactView:

Această vedere este utilizată pentru pagina de contact a site-ului.
Template-ul utilizat este "main/contact.html".
Utilizează un formular definit în "forms.py" pentru a permite utilizatorilor să trimită mesaje de contact.
Dacă utilizatorul completează și trimite cu succes formularul, acesta este redirecționat către pagina 
principală, iar un mesaj de succes este afișat.

"""

class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Mulţumim, vă vom contacta in cel mai scurt timp!')
		return super().form_valid(form)

"""

PortfolioView:

Această vedere este folosită pentru a afișa o listă de proiecte din portofoliu.
Template-ul utilizat este "main/portfolio.html".
Utilizează modelul Portfolio pentru a obține proiectele de portofoliu care sunt marcate 
ca active și le afișează pe pagină.

"""

class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

"""

PortfolioDetailView:

Această vedere afișează detaliile unui proiect specific din portofoliu.
Template-ul utilizat este "main/portfolio-detail.html".
Utilizează modelul Portfolio pentru a obține informații detaliate despre proiectul specific 
și le afișează pe pagină.

"""

class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

"""

BlogView:

Această vedere este folosită pentru a afișa o listă de articole de blog.
Template-ul utilizat este "main/blog.html".
Utilizează modelul Blog pentru a obține articolele de blog care sunt marcate ca active și 
le afișează pe pagină.

"""

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


"""

BlogDetailView:

Această vedere afișează detaliile unui articol specific de blog.
Template-ul utilizat este "main/blog-detail.html".
Utilizează modelul Blog pentru a obține informații detaliate despre articolul 
specific și le afișează pe pagină.

"""

class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"


"""

Aceste vederi sunt esențiale pentru funcționarea și afișarea conținutului site-ului web. 
Ele procesează cererile primite de la utilizatori și afișează paginile corespunzătoare, 
în funcție de URL-urile accesate. De asemenea, utilizează modelele definite pentru a accesa
și afișa date din baza de date a aplicației Django.

"""