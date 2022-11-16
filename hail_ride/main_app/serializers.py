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


class RiderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ('user', 'address', 'phone')


class DriverCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('user', 'current_address', 'phone')

class RideCreateSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(many=True)
    rider = RiderSerializer(many=True)
    
    class Meta:
        model = Ride
        fields=('driver',
                'rider',
                'start_time',
                'start_location',
                'end_location',
                'fare',
                'status',
                'payment_method')

class RideSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(many=True)
    rider = RiderSerializer(many=True)
    
    class Meta:
         model = Ride
         fields=('id',
                 'driver',
                'rider',
                'start_time',
                'start_location',
                'end_location',
                'status')
         
class ReviewSerializer(serializers.ModelSerializer):
    ride = RideSerializer(many=True)
    rider = RiderSerializer(many=True)
    driver= DriverSerializer(many=True)
    
    class Meta:
        model = Review
        fields = ('id',
                  'ride',
                  'rider',
                  'driver',
                  'rating',
                  'review',
                  'created_at',
                  'updated_at')