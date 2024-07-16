# Import path and include functions from Django
from django.urls import path, include
# Import DefaultRouter from Django REST Framework
from rest_framework.routers import DefaultRouter
# Import the viewsets from the views module
from .views import CompanyViewSet, ReviewViewSet
# Import the user-related views
from .views import UserCreate, MyTokenObtainPairView
# Import the TokenRefreshView for refreshing JWT tokens
from rest_framework_simplejwt.views import TokenRefreshView

# Create a router and register the Company and Review viewsets
router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'reviews', ReviewViewSet)

# Define the urlpatterns for the API
urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    path('register/', UserCreate.as_view(), name='register'),  # URL for user registration
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # URL for obtaining JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # URL for refreshing JWT token
]
