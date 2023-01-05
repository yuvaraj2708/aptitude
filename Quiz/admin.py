from django.contrib import admin
admin.site.site_header = "My Site"


# Register your models here.
from .models import *

admin.site.register(QuesModel)
admin.site.register(login)