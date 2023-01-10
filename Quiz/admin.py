from django.contrib import admin
from django_admin_listfilter_dropdown.filters import  RelatedDropdownFilter

admin.site.site_header = "My Site"


# Register your models here.
from .models import *


admin.site.register(QuesModel)
admin.site.register(login)
admin.site.register(Depart)

#samples
#sample
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Person)



class DepartmentAdmin(admin.ModelAdmin):
    
    list_display = ("__str__","Department")

    
    list_filter = (
         ('blog', RelatedDropdownFilter),
    )
fieldsets = (
        (None, {
            'fields': ('Depart_of', 'Role', 'python', 'C++')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('registration_required', 'depart.html'),
        }),
    ) 