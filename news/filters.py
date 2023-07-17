from django_filters import FiltersSet DateTimeFilter
from django.forms import Date TimeInput
from .models import New

class NewFilter(FiltersSet):
    added_after=DateTimeFilter(field_name='datepost',
                               lookup_expr='gt',
                               widget=DateTimeInput(format='%Y-%m-%dT%H:%M',
                                                    attrs={'type':'datetime-local'},
                                                    ),
                               )
    class Meta:
        model = New
        fields = {'name': ['icontains'],
                  'category': ['exact'],
                  }

