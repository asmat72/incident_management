from django.contrib import admin
from .models import Incident

class IncidentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'assigned_to', 'status', 'created_at']

admin.site.register(Incident, IncidentAdmin)

