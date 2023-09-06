"""

Acest fragment de cod este o clasă definită în Django care reprezintă un formular web utilizat 
pentru a colecta și valida datele introduse de utilizatori. Formularul este legat de modelul Django 
ContactProfile, ceea ce înseamnă că datele introduse de utilizator în acest formular vor fi validate 
și salvate în baza de date utilizând modelul ContactProfile.

"""

from django import forms
from .models import ContactProfile


"""

name, email, și message: Acestea sunt câmpurile formularului și sunt definite ca obiecte de 
formular Django. Fiecare câmp are specificate caracteristici precum tipul de widget (în acest 
caz, utilizat pentru afișarea formularului în HTML), limita maximă de caractere, necesitatea 
completării și un atribut de atribute pentru a afișa un text de încărcare în câmpul formularului.

"""

class ContactForm(forms.ModelForm):


	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..',
			'rows': 6,
			}))




	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)

"""

Meta: Aceasta este o clasă internă în formularul Django și este folosită pentru a specifica 
metadate despre formular, cum ar fi modelul cu care este legat (ContactProfile) și câmpurile 
din model care trebuie să apară în formular (fields). În acest caz, formularul va avea câmpuri 
pentru name, email și message, toate acestea provenind din modelul ContactProfile.

În ansamblu, acest formular (ContactForm) face mai ușoară crearea, validarea și gestionarea
datelor introduse de utilizatori atunci când aceștia transmit un mesaj de contact. Formularul poate 
fi apoi utilizat într-o vedere Django pentru a procesa datele introduse de utilizatori, de exemplu, pentru
a le salva în baza de date sau pentru a le utiliza în alte scopuri în aplicația ta.

"""