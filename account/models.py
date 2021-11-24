from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        # user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=70, null=True, blank=True)
    # full_name = models.CharField(max_length=120)
    # is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def create_activation_code(self):
        import hashlib
        string = self.email + str(self.id)
        encode_string = string.encode()
        md5_object = hashlib.md5(encode_string)
        activation_code = md5_object.hexdigest()
        print(activation_code)
        self.activation_code = activation_code
