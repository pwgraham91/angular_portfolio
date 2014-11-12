from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from a_port.api.permissions import IsOwnerOrReadOnly
from a_port.api.serializers import UserSerializer, ProjectSerializer
from rest_framework import status
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
    search_fields = ('id', 'title')
    filter_fields = ('id', 'title')
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        queryset = Project.objects.all()
        username = self.request.QUERY_PARAMS.get('username', None)
        if username is not None: # Optionally filters against 'username' query param
            queryset = queryset.filter(owner__username=username)
        return queryset

    def pre_save(self, obj):
        obj.owner = self.request.user

        # http://127.0.0.1:8000/projects/?owner__username=goldengate
        # http://127.0.0.1:8000/projects/?id=4

    @detail_route(methods=['post'])
    def follow(self, request, pk):
        project = Project.objects.get(pk=pk)
        # request.data.get comes from passing in data
        # follower_id = request.DATA.get('follower', None)
        # redefined follower_id as own user id
        follower_id = request.user.id
        project.follower.add(follower_id)
        return Response(status=status.HTTP_200_OK)