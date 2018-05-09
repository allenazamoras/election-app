from election.models import Party, User, Vote

from rest_framework import serializers


class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'name', 'detail')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'firstname', 'lastname')


class LoginSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class AppointSerializer(serializers.ModelSerializer):
    firstname = serializers.ReadOnlyField()
    lastname = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'username', 'firstname',
                  'lastname', 'party', 'position')


class VoteSerializer(serializers.ModelSerializer):
    party = serializers.ReadOnlyField(source='party.name')
    position = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('username', 'party', 'position')


class VoteAllSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    detail = serializers.ReadOnlyField()

    class Meta:
        model = Party
        fields = ('id', 'name', 'detail')


class CastVoteSerializer(serializers.ModelSerializer):
    firstname = serializers.ReadOnlyField(source='candidate.firstname')
    lastname = serializers.ReadOnlyField(source='candidate.lastname')
    position = serializers.ReadOnlyField(source='candidate.position')
    party = serializers.ReadOnlyField(source='candidate.party.name')

    class Meta:
        model = Vote
        fields = ('firstname', 'lastname', 'position', 'party')


class UnvoteSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='candidate.username')
    party = serializers.ReadOnlyField(source='candidate.party.name')
    position = serializers.ReadOnlyField(source='candidate.position')

    class Meta:
        model = Vote
        fields = ('id', 'username', 'party', 'position')


class ResultSerializer(serializers.ModelSerializer):
    vote = serializers.SerializerMethodField()
    party = serializers.ReadOnlyField(source='party.name')

    def get_vote(self, obj):
        count = Vote.objects.filter(candidate=obj).count()
        return count

    class Meta:
        model = User
        fields = ('username', 'party', 'position', 'vote')
