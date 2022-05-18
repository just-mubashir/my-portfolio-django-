from django.db import models
from ckeditor.fields import RichTextField
from base.models import BaseModel
# Create your models here.
class Blog(BaseModel):
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    code = RichTextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=False, help_text= 'check this box to publish post live')
    notes = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
