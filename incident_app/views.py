from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Incident 
from .forms import IncidentForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import IncidentSerializer

@login_required
def incident_list(request):
    incidents = Incident.objects.all()
    return render(request, 'incident_app/list.html', {'incidents': incidents})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'incident_app/register.html', {'form': form})

def incident_detail(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    form = IncidentForm(instance=incident)

    if request.method == 'POST':
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('incident-list')

    return render(request, 'incident_app/incident_detail.html', {
        'incident': incident,
        'form': form
    })

def create_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incident-list')
    else:
        form = IncidentForm()
    return render(request, 'incident_app/incident_detail.html', {'form': form})

class CreateIncident(APIView):
    def post(self, request):
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateIncident(APIView):
    def put(self, request, pk):
        try:
            incident = Incident.objects.get(pk=pk)
        except Incident.DoesNotExist:
            return Response({'error': 'Incident not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = IncidentSerializer(incident, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignIncident(APIView):
    def post(self, request, pk):
        try:
            incident = Incident.objects.get(pk=pk)
        except Incident.DoesNotExist:
            return Response({'error': 'Incident not found'}, status=status.HTTP_404_NOT_FOUND)

        incident.assigned_to = request.data.get('assigned_to')
        incident.status = 'assigned'
        incident.save()
        return Response({'message': 'Incident assigned successfully'})

class ResolveIncident(APIView):
    def post(self, request, pk):
        try:
            incident = Incident.objects.get(pk=pk)
        except Incident.DoesNotExist:
            return Response({'error': 'Incident not found'}, status=status.HTTP_404_NOT_FOUND)

        incident.status = 'resolved'
        incident.save()
        return Response({'message': 'Incident resolved successfully'})

#
from django.http import HttpResponse  

def index(request):
    return HttpResponse("Incident App is working!")
