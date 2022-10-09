from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_integer



class MyUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()

    middle_name = models.CharField(max_length=255,null=True, blank=True)
    phone_number = models.CharField(max_length=10, validators=[validate_integer])
    age = models.IntegerField(null=True)

    REQUIRED_FIELDS = [
        'date_of_birth',
        'first_name',
        'last_name',
        'phone_number',
        'email',
        ]

    def name(self):
        if self.middle_name:
            return str(self.first_name +  " " + self.middle_name + " " + self.last_name)
        
        return str(self.first_name + " " + self.last_name)