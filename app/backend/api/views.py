from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db import transaction
from django.contrib.auth import get_user_model
from .models import Company, Sentiment
from .serializers import (
    RegistrationSerializer,
    CompanySerializer,
    SentimentSerializer,
    # StatisticsSerializer,
    CustomTokenObtainPairSerializer,
)
from rest_framework import generics, permissions
from .models import SentimentAnalysis
from .serializers import SentimentAnalysisSerializer

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

class StatisticsView(generics.ListAPIView):
    serializer_class = SentimentAnalysisSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        company = self.request.user.company
        queryset = SentimentAnalysis.objects.filter(company=company)
        print("Number of records:", queryset.count())  # Log number of records
        for item in queryset:
            print(item.review)  # Log some sample data
        return queryset


# Obtaining JWT tokens
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer