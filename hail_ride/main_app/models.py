from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    # username = None
    email = models.EmailField(_('email address'), unique=True)

    UserNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Card(models.Model):
    holder_name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=16)
    card_type = models.CharField(max_length=10)
    card_expiration_date = models.DateField()
    pin = models.CharField(max_length=4)


class Rider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    home_address = models.CharField(max_length=200)
    current_address = models.CharField(max_length=200)
    driver_license = models.CharField(max_length=10)


class Ride(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_location = models.CharField(max_length=200)
    end_location = models.CharField(max_length=200)
    fare = models.FloatField()
    status = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=10)


class Review(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
