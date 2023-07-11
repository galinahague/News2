from django.shortcuts import render
from .models import New
from django.views.generic import ListView

# Create your views here.
class NewsList(ListView):
    model=New
    ordering='datepost'
    template_name='index.html'
    context_jbject_name='news'


def detail(request, slug):
    new = New.objects.get(slug__iexact=slug)
    return render (request, 'default.html', context={'new': new})