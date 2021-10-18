from rest_framework import serializers

from .models import User


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['user_id', 'password']

    def validate_user_id(self, user_id):
        if user_id == None:
            raise serializers.ValidationError('User not found')
        return user_id


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['user_id', 'name', 'email', 'password']
