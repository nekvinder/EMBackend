from rest_framework import serializers
from . models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'url', 'fullname', 'mobile', 'email',
                  'registration_type', 'idcard', 'group_id']


class IdCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdCard
        fields = ['id', 'url', 'imagepath']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'id', 'url']


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        fields = ['id', 'url', 'name', 'email', 'password']
