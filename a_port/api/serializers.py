__author__ = 'GoldenGate'
from rest_framework import serializers
from a_port.models import User, Project


class UserSerializer(serializers.ModelSerializer):
    project_count = serializers.SerializerMethodField('get_project_count')
    follower_list = serializers.SerializerMethodField('get_follower_list')
    class Meta:
        model = User
        # use these to explicitly set the fields in the api
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'date_joined', 'about', 'project_count')
        read_only_fields = ('date_joined', 'username')

    def get_project_count(self, obj):
        return obj.project.count()

    def get_follower_list(self, obj):
        print obj.project

    def validate_password(self, attrs, source):
        """
        Check that the password created is longer than 4 characters
        """
        password = attrs[source]
        if len(password)<4:
            raise serializers.ValidationError("SHORT!")
        return attrs

class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    follower = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Project

