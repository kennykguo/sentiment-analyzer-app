from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Company, Review
from .serializers import CompanySerializer, ReviewSerializer, UserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import CompanyStatisticsModel

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['get'])
    def statistics(self, request, pk=None):
        company = self.get_object()
        model = CompanyStatisticsModel('path/to/your/model.pth')
        statistics = model.calculate_statistics(company)
        return Response(statistics)

    @action(detail=True, methods=['post'], url_path='import-reviews')
    def import_reviews(self, request, pk=None):
        company = self.get_object()
        file = request.FILES['file']
        # Process the file and update reviews
        return Response({"status": "Reviews imported successfully"})

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
