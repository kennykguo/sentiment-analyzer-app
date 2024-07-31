"""
Contains views for user authentication logic
"""

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Get the custom user model if defined, otherwise use the default User model
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allows any user (authenticated or not) to access this view

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.filter(username=username).first()

    if user and user.check_password(password):
        # Generate JWT tokens for the authenticated user
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),  # Refresh token for obtaining new access tokens
            'access': str(refresh.access_token),  # Access token for authentication
        })

    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)