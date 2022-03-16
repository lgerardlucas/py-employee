from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from register.models import Register

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Register
        fields = ('__all__')
