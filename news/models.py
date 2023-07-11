from django.db import models
from django.shortcuts import revers

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    datepost = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('detail' kwargs={'slug': self.slug})