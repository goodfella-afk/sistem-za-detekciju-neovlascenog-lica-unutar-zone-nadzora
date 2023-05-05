from django.contrib import admin
from .models import Sistem

#this class is for better displayment in admin panel.
class StatusAdmin (admin.ModelAdmin):
    list_display = ['ids','aktivnost','status']


#this is call
admin.site.register(Sistem,StatusAdmin)


