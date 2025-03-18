from rest_framework import serializers
from .models import Message  # Your message model

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'  # Or list specific fields
