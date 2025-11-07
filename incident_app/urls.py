from django.urls import path
from .views import CreateIncident, UpdateIncident, AssignIncident, ResolveIncident
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),    
    path('', views.incident_list, name='incident-list'),
    path('create/', views.create_incident, name='create-incident'),
    path('create/', CreateIncident.as_view(), name='create-incident'),
    path('update/<int:pk>/', UpdateIncident.as_view(), name='update-incident'),
    path('assign/<int:pk>/', AssignIncident.as_view(), name='assign-incident'),
    path('resolve/<int:pk>/', ResolveIncident.as_view(), name='resolve-incident'),
    path('incident/<int:pk>/', views.incident_detail, name='incident-detail')
] 
