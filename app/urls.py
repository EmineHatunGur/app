from django.urls import path
from app.views import AppTemplateView,index

urlpatterns = [
    path('', index, name='about'), 
    path('about', AppTemplateView.as_view(), name='about'),
]