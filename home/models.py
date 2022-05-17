from django.db import models
from base.models import BaseModel

# Create your models here.

class Service(BaseModel):
    service_name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.service_name
       
class Contact(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, default="@gmail.com")
    phone = models.CharField(max_length=15, default='+91')
    city = models.CharField(max_length=15, default='Mumbai')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    text_message = models.TextField()
    def __str__(self):
        return f'Message from {self.name}, looking for {self.service.service_name}'
 
    