from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
admin.site.site_header = "My Site"


# Register your models here.
from .models import *

admin.site.register(QuesModel)
admin.site.register(login)
admin.site.register(Department)

class DepartmentAdmin(admin.ModelAdmin):
    search_fields=("Department_of")
    list_display=["Rolse_of"]
    list_filter =['DEVELOPER','IT']

class DepartmentAdmin(admin.ModelAdmin):
    
    list_filter = (
        # for ordinary fields
        ('a_charfield', DropdownFilter),
        # for choice fields
        ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('a_foreignkey_field', RelatedDropdownFilter),
    )
