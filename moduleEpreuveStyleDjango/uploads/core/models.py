from __future__ import unicode_literals
from django.db import models


class Document(models.Model):
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=100, default="nickname")
