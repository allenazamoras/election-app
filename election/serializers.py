from election.models import Party, User

from rest_framework import serializers


class PartySerializer(serializers.HyperlinkedModelSerializer):
    admin = serializers.ReadOnlyField(source='admin.username')

    class Meta:
        model = Party
        fields = ('id', 'name', 'detail', 'admin')


class AppointSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('position', 'party')

    def update(self, instance, validated_data):
        instance.position = validated_data.get('position', instance.position)
        instance.party = validated_data.get('party', instance.party)
        instance.save()
        return instance


class CreateUserSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password')
