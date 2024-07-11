# Import necessary modules and classes
from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Review
from .serializers import CompanySerializer, ReviewSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import CompanyStatisticsModel
from rest_framework.response import Response
from rest_framework.decorators import action

# Define a viewset for the Company model
class CompanyViewSet(viewsets.ModelViewSet):
    # Queryset of all companies
    queryset = Company.objects.all()
    # Serializer class for the Company model
    serializer_class = CompanySerializer

    # Define a custom action to get statistics for a company
    @action(detail=True, methods=['get'])
    def statistics(self, request, pk=None):
        # Get the specific company instance
        company = self.get_object()
        # Create an instance of the CompanyStatisticsModel with a placeholder path
        model = CompanyStatisticsModel('path/to/your/model.pth')
        # Calculate statistics for the company
        statistics = model.calculate_statistics(company)
        # Return the statistics as a response
        return Response(statistics)

# Define a viewset for the Review model
class ReviewViewSet(viewsets.ModelViewSet):
    # Queryset of all reviews
    queryset = Review.objects.all()
    # Serializer class for the Review model
    serializer_class = ReviewSerializer

# Define a view for user registration
class UserCreate(generics.CreateAPIView):
    # Queryset of all users
    queryset = User.objects.all()
    # Serializer class for the User model
    serializer_class = UserSerializer
    # Allow any user to access this view
    permission_classes = (AllowAny,)

# Define a view for obtaining JWT tokens
class MyTokenObtainPairView(TokenObtainPairView):
    # Custom serializer class for obtaining JWT tokens
    serializer_class = MyTokenObtainPairSerializer
