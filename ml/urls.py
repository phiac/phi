# ml/urls.py
from django.urls import path
from . import views

app_name = 'ml'  # Namespace for the app

urlpatterns = [
    path('sentiment/', views.sentiment_analysis_view, name='sentiment_analysis'),
    path('sentiment/view/', views.sentiment_analysis_view, name='sentiment_view'),  # Use this instead
]
