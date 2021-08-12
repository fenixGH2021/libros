from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    title_en = models.CharField(max_length=100)
    title_fr = models.CharField(max_length=100)
    autor = models.ManyToManyField(Autor)
    editorial = models.ManyToManyField(Editorial)

    class Meta:
        ordering = ['title_en']

    def __str__(self):
        return self.title_en
    