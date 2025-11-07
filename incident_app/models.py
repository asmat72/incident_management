from django.db import models
from django.utils import timezone

class Incident(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('assigned', 'Assigned'),
        ('resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(default=timezone.now)
