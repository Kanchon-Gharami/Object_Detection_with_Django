from django.db import models

class Image(models.Model):
    picture = models.ImageField(upload_to='images/')
    processed_picture = models.ImageField(upload_to='processed_images/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
