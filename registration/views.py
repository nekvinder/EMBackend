from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import viewsets
from . models import *
from . serializers import *


class RegistrationView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fullname', 'mobile', 'email',
                        'registration_type', 'idcard', 'group_id']


class IdCardView(viewsets.ModelViewSet):
    queryset = IdCard.objects.all()
    serializer_class = IdCardSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['imagepath']


class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class LoginView(viewsets.ModelViewSet):
    ''
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email', 'password']
