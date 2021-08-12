from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autores/', views.Autores, name='autores'),
    path('autores/crear-autor', views.crearAutor, name='crear-autor'),

    path('editoriales/', views.Editoriales, name='editoriales'),
    path('editoriales/crear-editorial', views.crearEditorial, name='crear-editorial'),

    path('libros/', views.Libros, name='libros'),
    path('libros/crear-libro', views.crearLibro, name='crear-libro'),
    path('libros/editar-libro/<int:pk>/', views.editarLibro, name='editar-libro'),

]
