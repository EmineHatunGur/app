from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    avatar=models.ImageField(upload_to='avatar/',)
    
    class Meta:
        verbose_name='Kullanıcı'
        verbose_name_plural='Kullanıcılar'

    def __str__(self):
        return self.username