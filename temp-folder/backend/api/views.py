from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db import transaction
from django.contrib.auth import get_user_model
from .models import Company, Sentiment, Statistics
from .serializers import (
    RegistrationSerializer,
    CompanySerializer,
    SentimentSerializer,
    StatisticsSerializer,
    CustomTokenObtainPairSerializer,
)

User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = serializer.save()
            return Response({
                "user": serializer.data,
                "message": "User registered successfully",
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "message": "Could not create user",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

# Returns the current company
class CompanyDataView(generics.RetrieveAPIView):
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user.company

# class SentimentListView(generics.ListCreateAPIView):
#     serializer_class = SentimentSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Sentiment.objects.filter(company=self.request.user.company)

#     def perform_create(self, serializer):
#         serializer.save(company=self.request.user.company)

# Returns the current statistics of the current company
class StatisticsView(generics.RetrieveUpdateAPIView):
    serializer_class = StatisticsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Statistics.objects.get(company=self.request.user.company)

# Obtaining JWT tokens
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer