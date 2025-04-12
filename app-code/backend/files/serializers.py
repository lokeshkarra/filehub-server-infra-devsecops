#files/serializers.py
from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()
    file_size = serializers.SerializerMethodField()  # Add file size field

    class Meta:
        model = File
        fields = ['id', 'file', 'uploaded_at', 'file_name', 'file_size']  # Include file_size
        read_only_fields = ['id', 'uploaded_at', 'file_name', 'file_size']

    def get_file_name(self, obj):
        return obj.file.name  # Access filename from the FileField

    def get_file_size(self, obj):
        return obj.size  # Access the size field from the File model
    

class FileDashboardSerializer(serializers.Serializer):
    total_files = serializers.IntegerField()
    total_storage_used = serializers.IntegerField()
    recent_uploads = FileSerializer(many=True)
    file_type_distribution = serializers.DictField(
        child=serializers.IntegerField()
    )