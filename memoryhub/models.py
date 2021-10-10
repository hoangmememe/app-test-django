from django.db import models
from django.contrib.auth.models import User

class Memory(models.Model):
    location = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
