#files/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count
from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from urllib.parse import quote
from django.utils.encoding import smart_str
from .models import File
from .serializers import FileSerializer, FileDashboardSerializer
from .utils import generate_presigned_url  # Import the utility function
from django.http import StreamingHttpResponse
import boto3

class FileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['GET'])
    def dashboard(self, request):
        files = self.get_queryset()
        # Total files and storage
        total_files = files.count()
        total_storage = files.aggregate(total_size=Sum('size'))['total_size'] or 0
        # Recent uploads (last 5)
        recent_uploads = files.order_by('-uploaded_at')[:5]
        # File type distribution
        file_type_distribution = files.values('file_type').annotate(count=Count('id'))
        distribution_dict = {
            item['file_type']: item['count']
            for item in file_type_distribution
        }
        data = {
            'total_files': total_files,
            'total_storage_used': total_storage,
            'recent_uploads': recent_uploads,
            'file_type_distribution': distribution_dict
        }
        serializer = FileDashboardSerializer(data)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def download(self, request, pk=None):
        file_instance = get_object_or_404(File, pk=pk, owner=request.user)
        bucket_name = 'filehub-media-s3'
        object_key = file_instance.file.name

        # Fetch the file from S3
        s3_client = boto3.client('s3')
        try:
            s3_object = s3_client.get_object(Bucket=bucket_name, Key=object_key)
            response = StreamingHttpResponse(
                s3_object['Body'].iter_chunks(),
                content_type=s3_object['ContentType']
            )
            # Set the Content-Disposition header with the correct filename
            response['Content-Disposition'] = f'attachment; filename="{smart_str(file_instance.filename)}"'
            return response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)