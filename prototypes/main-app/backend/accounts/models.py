"""
Handles user data structure
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields or methods here
    pass  # Currently uses default AbstractUser without modifications