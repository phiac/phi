# social_app/forms.py
# social_app/forms.py
from django import forms
from .models import VideoUpload, Video, UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)

class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoUpload  # Changed to VideoUpload if this form is for video uploads
        fields = ('title', 'video_file')
