from django.urls import path
from .views import CreateIncident, UpdateIncident, AssignIncident, ResolveIncident
from . import views

urlpatterns = [
    path('', views.index, name='incident-home'),
    path('create/', CreateIncident.as_view(), name='create-incident'),
    path('update/<int:pk>/', UpdateIncident.as_view(), name='update-incident'),
    path('assign/<int:pk>/', AssignIncident.as_view(), name='assign-incident'),
    path('resolve/<int:pk>/', ResolveIncident.as_view(), name='resolve-incident'),
] 
