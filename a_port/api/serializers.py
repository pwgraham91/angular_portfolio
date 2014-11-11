__author__ = 'GoldenGate'
from rest_framework import serializers
from a_port.models import User, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # use these to explicitly set the fields in the api
        # fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'date_joined', 'about')
        read_only_fields = ('date_joined', 'username')


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project