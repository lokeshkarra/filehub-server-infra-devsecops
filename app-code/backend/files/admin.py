from django.contrib import admin
from .models import File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['filename', 'owner', 'size', 'uploaded_at']
    list_filter = ['uploaded_at', 'owner']
    search_fields = ['filename', 'owner__username']
    readonly_fields = ['uploaded_at']
