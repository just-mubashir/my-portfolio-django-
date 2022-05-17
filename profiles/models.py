from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.FileField(upload_to='avator')
    def __str__(self):
        return self.user.username
    