from import_export import resources
from .models import Test

class PersonResource(resources.ModelResource):
    class Meta:
        model = Test