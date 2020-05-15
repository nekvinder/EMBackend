from rest_framework import serializers
from . models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id','fullname','mobile','email','registration_type','idcard','group_id']
        