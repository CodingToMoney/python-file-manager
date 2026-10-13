# app/models.py

from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    mime_type = models.CharField(max_length=100)

    def __str__(self):
        return self.file.name
