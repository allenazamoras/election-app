from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from election.models import Party, User
from election.serializers import PartySerializer, UserSerializer
from election.serializers import AppointSerializer
from election.serializers import LoginSerializer
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

    def create(self, request):
        req = request.POST
        user = User.objects.create_user(username=req['username'],
                                        password=req['password'],
                                        firstname=req['firstname'],
                                        lastname=req['lastname'])
        user.save()
        return Response(request.data)


class LoginView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def create(self, request):
        print(request.data['username'])
        print(request.data['password'])
        user = authenticate(username=request.data['username'],
                            password=request.data['password'])
        print(user)
        ret = {'return': 'Invalid Login credentials.'}
        if user is not None:
            if user.is_active:
                login(request, user)
                ret = {'return': request.data}
        return Response(ret)


class AppointViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = AppointSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          permissions.IsAdminUser,)

    def update(self, request, pk=None):
        obj = self.get_object()
        req = request.POST
        ret = {'return': "That position is already taken."}
        position = User.objects.all().filter(party=req['party'],
                                             position=req['position'])
        if not position:
            obj.position = req['position']
            obj.party = Party.objects.get(id=req['party'])
            obj.save(update_fields=['position', 'party'])
            serializer = AppointSerializer(obj)
            ret = {'return': serializer.data}
        return Response(ret)
