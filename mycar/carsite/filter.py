from django_filters.rest_framework import FilterSet
from .models import Car


class ProductFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'category': ['exact'],
            'active': ['exact'],
            'price': ['gt', 'lt']
        }