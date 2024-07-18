from django.urls import path
from .views import CompanyListCreateView, ReviewListCreateView

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
]
