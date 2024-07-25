# api/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company, Sentiment, Statistics

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
    company_name = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'company_name')

    def create(self, validated_data):
        company_name = validated_data.pop('company_name')
        user = User.objects.create_user(**validated_data)
        Company.objects.create(user=user, name=company_name)
        return user