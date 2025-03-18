 # social_app/forms.py
from django import forms
from .models import VideoUpload, Video, UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'video_file')

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = VideoUpload
        fields = ('title', 'video_file')
