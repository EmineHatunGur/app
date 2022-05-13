from django.db import models
from autoslug import AutoSlugField
from app.model.categorymodels import Category
from app.date_abstract_models import DateModel


class Article(DateModel):
    image = models.ImageField(upload_to='article_images')
    title = models.CharField(max_length=100, blank=False, null=False)
    contents = models.TextField()
    slug = AutoSlugField(populate_from='title', unique=True)
    categories = models.ManyToManyField(
        Category, max_length=100, related_name='article')
    writer = models.ForeignKey(
        'account.CustomUserModel', on_delete=models.CASCADE, related_name='articles')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return f"" .format(self.title, self.categories, self.writer)
