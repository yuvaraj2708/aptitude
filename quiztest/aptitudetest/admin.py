from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Test
# Register your models here.


admin.site.register(Profile)

@admin.register(Test)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('department', 'role', 'topic','question','answeroption','a','b','c','d')

admin.site.register(Hrlogin)

admin.site.register(Answer)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Topic)


