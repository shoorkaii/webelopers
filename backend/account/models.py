from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    user = models.ForeignKey(User, related_name='additionals')
    phone_number = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username + ': ' + self.phone_number
