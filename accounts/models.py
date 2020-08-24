from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.functional import cached_property


class UserManager(BaseUserManager):

    """
    Create and save user with email
    """

    def create_user(self, request_data, **kwargs):
        now = timezone.now()

        user = self.model(
            username=request_data['username'],
            is_active=True,
            last_login=now,
            date_joined=now,
        )

        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        request_data = {
            'username': username,
            'password': password
        }
        user = self.create_user(request_data)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    nickname = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='icon/',blank=True, null=True, default="images.png")

    @cached_property
    def get_profile(self):
        return self.objects.all()