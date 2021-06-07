from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    profile_name = models.CharField(blank=True, max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    def set_avatar(self):
        avatar = self.avatar
    if not avatar:
        self.avatar="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.phpfoxer.com%2Fproducts-and-services%2Fphpfox-default-avatar&psig=AOvVaw1jjvmCuoewtKu12MNKohTl&ust=1623158834058000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLiLh4HQhfECFQAAAAAdAAAAABAJ"

    def __str__(self):
        return self.email
