# api/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Company, Sentiment, Statistics
from .serializers import (
    RegistrationSerializer,
    CompanySerializer,
    SentimentSerializer,
    StatisticsSerializer,
)

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,)

class CompanyDataView(generics.RetrieveAPIView):
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user.company

class SentimentListView(generics.ListAPIView):
    serializer_class = SentimentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Sentiment.objects.filter(company=self.request.user.company)

class StatisticsView(generics.RetrieveAPIView):
    serializer_class = StatisticsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return Statistics.objects.get(company=self.request.user.company)