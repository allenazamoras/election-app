from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Party(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='register',
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='None')
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
    position = models.IntegerField(choices=PARTY_POSITION, default=0)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
