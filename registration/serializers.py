from rest_framework import serializers
from . models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id','fullname','mobile','email','registration_type','idcard','group_id']
        

class IdCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdCard
        fields = ['id','imagepath']


class GroupSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Group
        fields = ['name']

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        fields = ['id','name','email','password']

