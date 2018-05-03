from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from election.models import Party, User
from election.serializers import PartySerializer, UserSerializer
from election.serializers import AppointSerializer
#from election.serializers import LoginSerializer
from election.permissions import Appoint


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

"""
class LoginView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = LoginSerializer
"""

class AppointViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = AppointSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          permissions.IsAdminUser,)
