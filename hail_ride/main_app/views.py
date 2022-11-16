import sys

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from auth_app.serializers import UserCreateSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

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

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer


class RiderViewSet(ModelViewSet):
    queryset = Rider.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RiderCreateSerializer
        return RiderSerializer


class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DriverCreateSerializer
        return DriverSerializer
