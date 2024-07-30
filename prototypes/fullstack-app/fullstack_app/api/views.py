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
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from django.db import transaction

# class RegistrationView(generics.CreateAPIView):
#     serializer_class = RegistrationSerializer
#     permission_classes = (permissions.AllowAny,)

#     def create(self, request, *args, **kwargs):
#         print("Request data:", request.data)  # Debugging line
#         serializer = self.get_serializer(data=request.data)
#         if not serializer.is_valid():
#             print("Serializer errors:", serializer.errors)  # Debugging line
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        print("Request data:", request.data)  # Debugging line
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("Serializer errors:", serializer.errors)  # Debugging line
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = serializer.save()
            print(f"User created: {user.username}, ID: {user.id}")  # Debugging line
            return Response({
                "user": serializer.data,
                "message": "User registered successfully",
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error creating user: {str(e)}")  # Debugging line
            return Response({
                "message": "Could not create user",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)




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



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer