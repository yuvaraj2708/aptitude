from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person
# Register your models here.


admin.site.register(Profile)

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('department', 'role', 'topic','question','answeroption','a','b','c','d')