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
        fields = ('id','user', 'address', 'phone')


class DriverSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )

    class Meta:
        model = Driver
        fields = ('user', 'phone', 'current_address', 'home_address')


class CardSerializer(serializers.ModelSerializer):
    rider = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='rider-detail'
    )

    class Meta:
        model = Card
        fields = ('rider', 'id', 'card_number', 'card_expiry_date', 'card_cvv', 'card_type')


class RideSerializer(serializers.ModelSerializer):
    driver = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='driver-detail'
    )
    rider = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='rider-detail'
    )

    class Meta:
        model = Ride
        fields = ('driver', 'rider', 'start_address', 'end_address', 'start_time', 'end_time', 'fare', 'status')


class ReviewSerializer(serializers.ModelSerializer):
    driver = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='driver-detail'
    )
    rider = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='rider-detail'
    )

    class Meta:
        model = Review
        fields = ('driver', 'rider', 'rating', 'comment')


class RiderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ('user', 'address', 'phone')


class DriverCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('user', 'current_address', 'phone')


class CardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('rider', 'card_number', 'card_expiry_date', 'card_cvv', 'card_type')


class RideCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('driver', 'rider', 'start_address', 'end_address', 'start_time', 'end_time', 'fare', 'status')


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('driver', 'rider', 'rating', 'comment')

