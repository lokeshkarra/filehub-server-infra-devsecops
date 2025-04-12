from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile

def validate_file_type(file):
    if file.content_type not in settings.ALLOWED_FILE_TYPES:
        raise ValidationError(f'File type {file.content_type} is not allowed.')

class File(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='files'
    )
    file = models.FileField(
        upload_to='user_files/',
        validators=[validate_file_type]
    )
    filename = models.CharField(max_length=255)
    size = models.BigIntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.filename:
            self.filename = self.file.name
        if not self.size:
            self.size = self.file.size

        # Determine file type
        if isinstance(self.file, InMemoryUploadedFile):
            self.file_type = self.file.content_type
        else:
            self.file_type = 'unknown'

        # Update user's storage
        user = self.owner
        user.storage_used += self.size
        user.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Reduce user's storage when file is deleted
        user = self.owner
        user.storage_used -= self.size
        user.save()

        self.file.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.filename