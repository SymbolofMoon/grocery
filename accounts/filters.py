

from .models import Item
import django_filters

class GroceryFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['name' ]