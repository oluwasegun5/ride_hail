from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',)
        extra_kwargs = {'password': {'write_only': True}}


class RiderSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )

    class Meta:
        model = Rider
        fields = ('user', 'address', 'phone')


class DriverSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )

    class Meta:
        model = Driver
        fields = ('user', 'phone', 'current_address', 'home_address')


class RiderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ('user', 'address', 'phone')


class DriverCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('user', 'current_address', 'phone')
