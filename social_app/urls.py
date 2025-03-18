from django.urls import path
from . import views

app_name = 'social_app'

urlpatterns = [
    path('video_feed/', views.video_feed, name='video_feed'),
    path('feed/', views.feed_view, name='feed'),
    path('upload/', views.upload_video_view, name='upload_video'),
    path('video_upload/', views.upload_video_form_view, name='upload_video_form'),
    path('upload_view/', views.upload_view, name='social_upload'),  # Correct name
]
