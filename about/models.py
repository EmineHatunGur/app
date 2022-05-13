from django.urls import reverse
from django.db import models
from django.utils.translation import gettext as _

class About (models.Model):
    
    title=models.CharField(max_length=150)
    text=models.TextField()
    

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")

   

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


