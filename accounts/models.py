from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.functional import cached_property


class User(AbstractUser):
    nickname = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='icon/',blank=True, null=True, default="images.png")


    @cached_property
    def get_profile(self):
        return self.objects.all()