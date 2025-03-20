from django.contrib import admin
from django.urls import path, include
from xvoice import views
from django.conf import settings
from django.conf.urls.static import static
from xvoice.views import CustomLoginView
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path('process_voice/', views.process_voice, name='process_voice'),
    path('machine_learning/', views.machine_learning_view, name='machine_learning'),
    path('messaging_view/', include('messaging.urls')),  # Include app URLs
    path('ml/', include('ml.urls')),
    path('query_search/', include('query_search.urls')),
    path('login/', include('django.contrib.auth.urls')),  # Login-related URLs
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('social_app/', include('social_app.urls', namespace='social_app')),
    path('', include('xvoice.urls')),  # Include xvoice app URLs
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
