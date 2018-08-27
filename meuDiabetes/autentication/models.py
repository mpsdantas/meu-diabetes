from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    class Meta:
        unique_together = ('email',)
# Create your models here.
