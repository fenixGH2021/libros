from django.shortcuts import render, redirect
from .models import Autor, Editorial, Libro
from .forms import AutorForm, EditorialForm, LibroForm

# Create your views here.
def index(request):
    return render(request, 'libros/index.html')

def Autores(request):
    autores = Autor.objects.all()
    context = {
        'autores': autores
    }
    return render(request, 'libros/autores.html', context)

def crearAutor(request):
    title = 'Crear Autores'
    form = AutorForm()
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autores')

    context = {
        'form': form,
        'title': title
    }
    return render(request, 'libros/autor-form.html', context)


def Editoriales(request):
    editoriales = Editorial.objects.all()
    context = {
        'editoriales': editoriales
    }
    return render(request, 'libros/editoriales.html', context)

def crearEditorial(request):
    title = 'Crear Editoriales'
    form = EditorialForm()
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('editoriales')

    context = {
        'form': form,
        'title': title
    }
    return render(request, 'libros/editorial-form.html', context)

def Libros(request):
    libros = Libro.objects.all()
    context = {
        'libros': libros
    }
    return render(request, 'libros/libros.html', context)

def crearLibro(request):
    title = 'Crear Libros'
    form = LibroForm()
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros')

    context = {
        'form': form,
        'title': title
    }
    return render(request, 'libros/libro-form.html', context)

def editarLibro(request, pk):
    libro = Libro.objects.get(id=pk)
    context = {
        'libro': libro,
    }
 
    return render(request, 'libros/editar-libro.html', context)