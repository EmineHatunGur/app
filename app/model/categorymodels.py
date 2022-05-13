from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    category_name = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from='category_name', unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
