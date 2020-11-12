from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import UserManager
# Create your models here.

class User (AbstractUser):
    """Implementacion custom de usuario para modificar
    flujo de creacion y activacion de usuario"""
    
    username = None
    password = models.CharField(max_length=128, null=True)
    email = models.EmailField('Email', unique=True)
    phone_number = models.CharField('Numero Telefono', max_length=15)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 
        'last_name',
        'phone_number'
    ]

    def __str__(self):
        return self.username