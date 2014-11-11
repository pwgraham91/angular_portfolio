from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from a_port.api.serializers import UserSerializer, ProjectSerializer

__author__ = 'GoldenGate'
from rest_framework import viewsets
from a_port.models import User, Project

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'about')
    # /users/?search=rudy searches across all listed fields
    # /users/?ordering=first_name orders by first name alphabetically
    ordering_fields = ('first_name', 'last_name')
    # /users/ default ordering is by the highest id
    ordering = ('-id',)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_queryset(self):
        queryset = Project.objects.all()
        username = self.request.QUERY_PARAMS.get('username', None)
        if username is not None: # Optionally filters against 'username' query param
            queryset = queryset.filter(owner__username=username)
        return queryset

    def pre_save(self, obj):
        obj.owner = self.request.user