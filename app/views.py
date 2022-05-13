from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from about.models import About

def index(request):
    return HttpResponse('merhaba')



class AppTemplateView(TemplateView):
    model=About
    template_name='about.html'

    def get_context_data(self, **kwargs):
          
            context = super().get_context_data(**kwargs)
            context["name"] =About.objects.get(id=1)
            context["data"] ="Merhaba Dünya"
            return context
        
      



