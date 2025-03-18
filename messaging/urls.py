from django.urls import path
from . import views


app_name = 'messaging'
urlpatterns = [
     path('messaging_view/', views.messaging_messaging_view, name='messaging_messaging'),
 ]
