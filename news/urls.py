from django.urls import path
from .views import NewsList, detail

urlpatterns = [path('', NewsList,as_view()),
               path('new/<str:slug>', detail, name='detail')