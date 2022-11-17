import sys

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from auth_app.serializers import UserCreateSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import permissions


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(deactivate=False)


    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(user.password)
        user.save()

        subject = 'welcome to HailRide world'
        message = f'Hi {self.request.data.get("first_name")}, thank you for registering in HailRide.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.request.data.get("email"), ]
        send_mail(subject, message, email_from, recipient_list)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.deactivate = True
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer
    
    def get_permissions(self):
        if self.request.method != 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
            


class RiderViewSet(ModelViewSet):
    queryset = Rider.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RiderCreateSerializer
        return RiderSerializer


class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DriverCreateSerializer
        return DriverSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_serializer_class(self):
        # if self.request.method == 'POST':
        #     return CardCreateSerializer
        return CardCreateSerializer


class RideViewSet(ModelViewSet):
    queryset = Ride.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RideCreateSerializer
        return RideSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReviewCreateSerializer
        return ReviewSerializer
