from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name','last_name','email', )
        extra_kwargs = {'password': {'write_only': True}}
  

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id',
                  'review',
                  'created_at',
                  'updated_at',
                  'deleted_at')

class RiderSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )

    review = ReviewSerializer(many=True)
    class Meta:
        model = Rider
        fields = ('user', 'review', 'phone', 'address')


class DriverSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )
    review = ReviewSerializer(many=True)

    class Meta:
        model = Driver
        fields = ('id', 'review', 'user', 'phone', 'current_address', 'home_address')
        read_only_fields = ('re')

class RiderCreateSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True)
    class Meta:
        model = Rider
        fields = ('id', 'review', 'user', 'address', 'phone')


class DriverCreateSerializer(serializers.ModelSerializer):
     review = ReviewSerializer(many=True)
     class Meta:
        model = Driver
        fields = ('id', 'review','user', 'phone','home_address','current_address', 'driver_license')
