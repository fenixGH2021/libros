from django.forms import ModelForm
from .models import Autor, Libro, Editorial

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email']

class EditorialForm(ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre']

class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['title_en', 'title_fr', 'autor', 'editorial']
