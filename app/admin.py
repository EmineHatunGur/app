from django.contrib import admin
from app.model.articlemodels import  Article
from app.model.categorymodels import Category
from app.model.commentmodels import  Comment
from app.model.iletisim import IletisimModel




admin.site.register(Category)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'contents')
    list_display = ('title', 'creation_date', 'upload_date')


admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('comment_writer', 'creation_date', 'upload_date')
   


admin.site.register(Comment, CommentAdmin)

class IletisimAdmin(admin.ModelAdmin):
    
    list_display = ('email','name_surname', 'creation_date', )
   


admin.site.register(IletisimModel, IletisimAdmin)

