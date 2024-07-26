# api/views.py
from rest_framework import status
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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