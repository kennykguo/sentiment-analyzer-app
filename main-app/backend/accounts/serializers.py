"""
Serializes user data for API interactions
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}  # Ensures password is write-only

    def create(self, validated_data):
        # Use create_user to properly hash the password
        user = User.objects.create_user(**validated_data)
        return user