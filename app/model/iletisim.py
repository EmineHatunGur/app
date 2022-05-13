from tabnanny import verbose
from django.db import models


class IletisimModel(models.Model):
    email=models.EmailField(max_length=254,blank=True,null=True)
    name_surname=models.CharField(max_length=150)
    mesaj=models.TextField()
    creation_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='iletisim'
        verbose_name_plural='iletisims'

    def __str__(self):
        return self.email