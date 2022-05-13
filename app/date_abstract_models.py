from django.db import models

class DateModel(models.Model):
    creation_date=models.DateTimeField(auto_now_add=True)
    upload_date=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True