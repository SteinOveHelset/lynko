from django.contrib.auth.models import AbstractUser
from django.db import models
from djstripe.models import Customer, Subscription


class Plan(models.Model):
    name = models.CharField(max_length=255)
    max_num_links = models.IntegerField()


class User(AbstractUser):
    plan = models.ForeignKey(Plan, related_name='users', default=1, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    subscription = models.ForeignKey(Subscription, null=True, blank=True,on_delete=models.SET_NULL)