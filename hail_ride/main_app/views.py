import sys
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from auth_app.serializers import UserCreateSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            subject = 'welcome to HailRide world'
            message = f'Hi {self.request.data.get("first_name")}, thank you for registering in HailRide.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [self.request.data.get("email"), ]
            send_mail(subject, message, email_from, recipient_list)
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
