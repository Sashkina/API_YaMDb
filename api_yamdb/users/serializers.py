from rest_framework import serializers

from .models import User


class ConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'bio', 'email',
                  'role')
        lookup_field = 'username'


class UserPATCHSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'bio', 'email')
        lookup_field = 'username'


class ConfirmationCodeSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()
