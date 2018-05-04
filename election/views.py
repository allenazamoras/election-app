from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from election.models import Party, User, Vote
from election.serializers import PartySerializer, UserSerializer
from election.serializers import AppointSerializer, VoteAllSerializer
from election.serializers import LoginSerializer, VoteSerializer
from election.permissions import Appoint


class PartyViewSet(viewsets.ModelViewSet):
    """
    This view automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


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
        ret = {'success': 0}

        if user is not None:
            if user.is_active:
                login(request, user)
                ret = {'return': request.data, 'success': 1,
                       'session': request.session.session_key}
        print(request.session.set_test_cookie())
        return Response(ret)


class AppointViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AppointSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          permissions.IsAdminUser,)

    def update(self, request, pk=None):
        obj = self.get_object()
        req = request.POST
        ret = {'return': 'That position is already taken.'}
        position = User.objects.all().filter(party=req['party'],
                                             position=req['position']).exclude(
            party=Party.objects.get(name='Independent'))

        if not position:
            obj.position = req['position']
            obj.party = Party.objects.get(id=req['party'])
            obj.save(update_fields=['position', 'party'])
            serializer = AppointSerializer(obj)
            ret = {'return': serializer.data}
        return Response(ret)


class VoteViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().exclude(position=0)
    serializer_class = VoteSerializer

    def create(self, request):
        req = request.POST
        user = User.objects.get(username=request.user)
        candidate = User.objects.get(username=req['username'])
        candidate2 = User.objects.filter(position=candidate.position).first()
        voted = Vote.objects.filter(user=request.user,
                                    candidate=candidate2)

        ret = {'return': "You've already voted for this position"}
        if not voted:
            vote = Vote(user=user, candidate=candidate)
            vote.save()
            ret = {'return': 'Successfully voted for candidate'}
        return Response(ret)


class VoteAllViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = VoteAllSerializer

    def create(self, request):
        req = request.POST
        party = Party.objects.get(name=req['name'])
        candidate_set = User.objects.all().filter(party=party)

        ret = {'return': 'No available candidates for this party.'}
        if candidate_set:
            ret = {'return': 'You have voted for every candidate'
                             'in this party.'}
            user = User.objects.get(username=request.user)
            for user in user_set:
                pass
                #candidate = User.objects.get(username=user.username)
                #vote = Vote(user=user, candidate=candidate)
                #vote.save()
        return Response(ret)
