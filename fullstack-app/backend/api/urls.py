from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    # We need a custom view for obtaining JWT tokens since we authenticate with email and password, not user and password
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('company/', views.CompanyDataView.as_view(), name='company_data'),
    path('statistics/', views.StatisticsView.as_view(), name='statistics'),
    # path('sentiments/', views.SentimentListView.as_view(), name='sentiment_list'),
]