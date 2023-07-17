from django.shortcuts import render
from .models import New
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import NewFilter
from .forms import NewForm
from django.urls import reverse_lazy

# Create your views here.
class NewsList(ListView):
    model=New
    ordering='datepost'
    template_name='news/index.html'
    context_object_name='news'
    paginate_by = 10

def get_queryset(self):
    queryset=super().get_queryset()
    self.filterset=NewFilter(self.request.GET, queryset)
    return self.filterset.qs

def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs):
    context['filterset']=self.filterset
    return context

class NewDetail(DetailView):
    model = New
    template = 'news/index.html'
    context_object_name= 'news'


class NewCreate(CreateView):
    form_class=NewForm
    model = New
    template_name='news/news_edit.html'


class NewUpdate(UpdateView):
    form_class=NewForm
    model = New
    template_name = 'news/news_edit.html'


class NewDelete(DeleteView):
    model = New
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news_list')



def detail(request, slug):
    new = New.objects.get(slug__iexact=slug)
    return render (request, 'default.html', context={'new': new})