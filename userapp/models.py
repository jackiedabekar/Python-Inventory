from enum import unique
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.deletion import DO_NOTHING
from .managers import UserManager, AllUserManager
from django.contrib.auth.models import Group
from django.conf import settings


class UserType(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs) :
        self.name = self.name.lower()
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'user-type'
        unique_together = ['name']


class User(AbstractBaseUser, PermissionsMixin):
    """
    User Model
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    user_type = models.ForeignKey(UserType,
                                 on_delete=models.DO_NOTHING,
                                 blank=True,
                                 null=True,
                                 related_name='UserType')
    is_admin  = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    all_objects = AllUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']
        db_table = 'users'
   
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs) :
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    def delete(self):
        self.is_active = False
        self.save()
