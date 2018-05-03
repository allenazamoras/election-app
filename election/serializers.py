from election.models import Party, User

from rest_framework import serializers
from rest_framework.response import Response


class PartySerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Party
        fields = ('id', 'name', 'detail', 'creator')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'firstname', 'lastname')


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')


class AppointSerializer(serializers.ModelSerializer):
    firstname = serializers.ReadOnlyField()
    lastname = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'username', 'firstname',
                  'lastname', 'party', 'position')
