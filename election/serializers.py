from election.models import Party, User

from rest_framework import serializers


class PartySerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Party
        fields = ('id', 'name', 'detail', 'creator')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        password = serializers.CharField(write_only=True)
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.set_firstname(validated_data['firstname'])
        user.set_lastname(validated_data['lastname'])
        user.save()
        return user
        

    class Meta:
        model = User
        fields = ('username', 'password', 'firstname', 'lastname')
