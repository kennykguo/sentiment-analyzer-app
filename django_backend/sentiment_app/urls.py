from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the index page
    path('', views.index, name='index'),
    # URL pattern for the result page
    path('result/<str:sentiment_id>/', views.result, name='result'),
    # URL pattern for deleting a sentiment
    path('delete/<str:sentiment_id>/', views.delete, name='delete'),
]