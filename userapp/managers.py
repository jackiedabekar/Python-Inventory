from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group


##### User manager #####
class UserManager(BaseUserManager):
    use_in_migration = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('Email is required')

        # if 'group' in extra_fields :
        #     group = extra_fields.pop('group')
        # print(extra_fields)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        # print(**extra_fields)
        return user

    # django -> Creating a normal user
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    # django -> Creating a super user with createsuperuser command
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def create(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class AllUserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset()
