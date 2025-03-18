# query_search/urls.py
from django.urls import path
from . import views

app_name = 'query_search'  # Namespace for the app

urlpatterns = [
    path('view/', views.query_search_view, name='query_search_view'),
    path('search/', views.query_search_view, name='search'),
]
