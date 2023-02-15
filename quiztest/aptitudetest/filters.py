import django_filters

from .models import *


class TestFilter(django_filters.FilterSet):
    class Meta:
        model=Test
        fields = [
            'department',
            'role',
            'topic',
            
        ]