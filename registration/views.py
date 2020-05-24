from django.shortcuts import render
from rest_framework import viewsets
from . models import *
from . serializers import *


class RegistrationView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class IdCardView(viewsets.ModelViewSet):
    queryset = IdCard.objects.all()
    serializer_class = IdCardSerializer

class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    
class LoginView(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    