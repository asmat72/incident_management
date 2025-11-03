from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Incident
from .serializers import IncidentSerializer

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
