from django.db import models
from app.model.articlemodels import Article
from app.date_abstract_models import DateModel


class Comment(DateModel):
    comment_writer = models.ForeignKey(
        'account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
    contents = models.ForeignKey(
        Article, on_delete=models.CASCADE)
    comment=models.TextField()
   

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
            return f"" .format(self.comment_writer)
