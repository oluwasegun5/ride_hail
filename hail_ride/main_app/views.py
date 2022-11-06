import sys
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from auth_app.serializers import UserCreateSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

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
