# api/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationView, CompanyDataView, SentimentListView, StatisticsView
from .views import CustomTokenObtainPairView

from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Test view reached")


urlpatterns = [
    path('test/', test_view, name='test'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('company/', CompanyDataView.as_view(), name='company_data'),
    path('sentiments/', SentimentListView.as_view(), name='sentiment_list'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]