from django.shortcuts import render
from rest_framework import viewsets
from . models import Registration
from . serializers import RegistrationSerializer

class RegistrationView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    