from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Party(models.Model):
    name = models.CharField(max_length=100, blank=True, default='Independent')
    detail = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


class User(AbstractUser):
    PARTY_POSITION = (
        (0, "N/A"),
        (1, "President"),
        (2, "Vice-President"),
        (3, "Secretary"),
        (4, "Assistant-Secretary"),
        (5, "Treasurer"),
        (6, "Assistant-Treasurer"),
        (7, "PRO"),
    )
    position = models.SmallIntegerField(choices=PARTY_POSITION, default=0)
    party = models.ForeignKey(Party, on_delete=models.CASCADE,
                              blank=True, null=True, related_name='party')
    firstname = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.username


class Vote(models.Model):
    candidate = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='candidate')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user')

