from django.db import models
from django.utils import timezone
from precise_bbcode.fields import BBCodeTextField

class Post(models.Model):
    auteur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="titre")
    image = models.FileField(upload_to = 'post/', default='jre2017.png')
    text = BBCodeTextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True, verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
         return self.nom