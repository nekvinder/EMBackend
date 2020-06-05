from rest_framework import serializers
from . models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'url', 'fullname', 'mobile', 'email',
                  'registration_type', 'idcard', 'group_id', 'created_at', 'created_at', 'updated_at']


class IdCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdCard
        fields = ['id', 'url', 'imagepath']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'id', 'url','eventId']


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        fields = ['id', 'url', 'name', 'email', 'password']


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'url', 'name', 'description', 'start', 'end']
