from django.contrib import admin
from .models import Incident

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'assigned_to')

admin.site.register(Incident, IncidentAdmin)

