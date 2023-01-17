from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(blank=True, verbose_name="Direccion", null=True, max_length=200)
    cellphone = models.CharField(max_length=10, blank=True, verbose_name="Telefono", null=True)

    def __str__(self):
        return f"{self.user.username} {self.user.first_name}"

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'