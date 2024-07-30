"""
Defines URL patterns for user authentication endpoints
URLs are used to return the user to a certain view
"""

from django.urls import path
from .views import RegisterView, login_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Class-based view needs .as_view()
    path('login/', login_view, name='login'),
]