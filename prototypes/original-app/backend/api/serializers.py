# Import the serializers module from Django REST Framework
from rest_framework import serializers
# Import the Company and Review models
from .models import Company, Review
# Import the User model from Django's authentication system
from django.contrib.auth.models import User
# Import the TokenObtainPairSerializer for JWT authentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Define a serializer for the Company model
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# Define a serializer for the Review model
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# Define a serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Define a custom serializer for obtaining JWT tokens
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Get the standard token
        token = super().get_token(user)
        # Add the username to the token
        token['username'] = user.username
        return token
