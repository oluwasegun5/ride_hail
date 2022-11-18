from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    deactivate = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)


class Card(models.Model):
    rider = models.ForeignKey('Rider', on_delete=models.CASCADE, default=None)
    card_number = models.CharField(max_length=16)
    card_holder_name = models.CharField(max_length=100, default='')
    card_expiry_date = models.DateField(default=None)
    card_cvv = models.CharField(max_length=3, default=None)
    card_type = models.CharField(max_length=10, default=None)


class Rider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.user


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    home_address = models.CharField(max_length=200)
    current_address = models.CharField(max_length=200)
    driver_license = models.CharField(max_length=10)

    def __str__(self):
        return self.user


class Ride(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    start_address = models.CharField(max_length=200)
    end_address = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    fare = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.start_address} to {self.end_address}"


class Review(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, default=None)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, default=None)
    rating = models.IntegerField(default=0)
    comment = models.CharField(max_length=200, default=None)
    date = models.DateTimeField(default=None)

    def __str__(self):
        return self.comment
