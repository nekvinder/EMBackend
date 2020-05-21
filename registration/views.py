from django.shortcuts import render
from rest_framework import viewsets
from . models import Registration
from . models import IdCard
from . models import Group
from . serializers import RegistrationSerializer
from . serializers import IdCardSerializer
from . serializers import GroupSerializer

class RegistrationView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class IdCardView(viewsets.ModelViewSet):
    queryset = IdCard.objects.all()
    serializer_class = IdCardSerializer

class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    