from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins

from election.models import Party, User
from election.permissions import Appoint
from election.serializers import PartySerializer, CreateUserSerializer
from election.serializers import AppointSerializer


class PartyViewSet(viewsets.ModelViewSet):
    """
    This view automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, Appoint,)

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)


class AppointView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = AppointSerializer


class CreateUserView(generics.CreateAPIView):

    model = User
    serializer_class = CreateUserSerializer
    permission_classes = (permissions.AllowAny,)
