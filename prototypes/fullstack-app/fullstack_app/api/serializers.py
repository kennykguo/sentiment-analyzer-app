# api/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company, Sentiment, Statistics
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')

class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentiment
        fields = ('id', 'review')

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ('id', 'mean', 'standard_deviation')

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    company_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'company_name')

    def create(self, validated_data):
        company_name = validated_data.pop('company_name')
        user = User.objects.create_user(**validated_data)
        Company.objects.create(user=user, name=company_name)
        return user


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     email = serializers.EmailField(required=True)

#     def validate(self, attrs):
#         try:
#             user = User.objects.get(email=attrs['email'])
#         except User.DoesNotExist:
#             raise serializers.ValidationError('User with this email does not exist.')
        
#         attrs['username'] = user.username  # Set username in attrs for authentication
#         return super().validate(attrs)
# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     username_field = 'email'

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')

#         if email and password:
#             user = User.objects.filter(email=email).first()
#             if user:
#                 if user.check_password(password):
#                     attrs['username'] = user.username
#                     return super().validate(attrs)
#             raise serializers.ValidationError('No active account found with the given credentials')
#         else:
#             raise serializers.ValidationError('Must include "email" and "password".')

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     username_field = User.EMAIL_FIELD

#     def validate(self, attrs):
#         credentials = {
#             'email': attrs.get('email'),
#             'password': attrs.get('password')
#         }

#         user = User.objects.filter(email=credentials['email']).first()
#         if user and user.check_password(credentials['password']):
#             attrs['username'] = user.username
#             return super().validate(attrs)
#         else:
#             raise serializers.ValidationError('No active account found with the given credentials')
        

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)
            if not user:
                raise serializers.ValidationError('No active account found with the given credentials')

            attrs['username'] = user.username
            return super().validate(attrs)
        else:
            raise serializers.ValidationError('Must include "email" and "password".')