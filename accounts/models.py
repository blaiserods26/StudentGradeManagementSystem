from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    STUDENT = 'student'
    MANAGEMENT = 'management'
    
    USER_TYPE_CHOICES = [
        (STUDENT, 'Student'),
        (MANAGEMENT, 'Management'),
    ]
    
    identification_number = models.CharField(max_length=20, unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=STUDENT)
    
    USERNAME_FIELD = 'identification_number'
    REQUIRED_FIELDS = ['username', 'email'] 