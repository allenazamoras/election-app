from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions

from election.models import Party, User
from election.serializers import PartySerializer, UserSerializer


class PartyViewSet(viewsets.ModelViewSet):
    """
    This view automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
