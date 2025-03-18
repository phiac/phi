from django.shortcuts import render, redirect
from .forms1 import VideoUploadForm, VideoForm, FileUploadForm
from .forms import VideoForm, FileUploadForm
from .models import VideoUpload, Video, UploadedFile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.apps import apps
import aiortc
print("aiortc installed successfully!")


@login_required
def upload_video_view(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('feed')  # Redirect to the feed page after upload
    else:
        form = VideoUploadForm()
    return render(request, 'upload_video.html', {'form': form})

def video_feed(request):
    videos = Video.objects.all().order_by('-uploaded_at')
    return render(request, 'video_feed.html', {'videos': videos})

def feed_view(request):
    videos = Video.objects.all().order_by('-uploaded_at')  # Adjusted field name
    return render(request, 'feed.html', {'videos': videos})

def upload_video_form_view(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('feed')  # Redirect to the feed page after upload
    else:
        form = VideoForm()
    return render(request, 'social_app/upload_video.html', {'form': form})

@login_required
def upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('social_app:social_upload')  # Use the correct URL name
    else:
        form = FileUploadForm()

    return render(request, 'social_upload.html', {'form': form})
