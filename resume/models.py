from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Description(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    avator = models.FileField(default="media/no_img.png", upload_to='avator')
    about_user = RichTextField()
    d_o_b = models.DateField()
    job_role = models.CharField(max_length=255,null=True,blank=True )
    languages_speak = models.CharField(max_length=255)
    def __str__(self):
        return self.user.username
    
class Experience(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    organization = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    technologies = RichTextField()
    roles = RichTextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active_job = models.BooleanField(default=True)
    def __str__(self):
        return f'Name: {self.user.username}, organization : {self.organization}'
class Education(BaseModel):
    title = models.CharField(max_length=255)
    university_name = models.CharField(max_length=255)
    city= models.CharField(max_length=255,null=True,blank=True)
    country = models.CharField(max_length=255, null=True,blank=True)
    subjects = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year_of_joining = models.DateField(null=True,blank=True)
    year_of_passing = models.DateField(null=True,blank=True)
    def __str__(self):
        return f'Name: {self.user.username}, title : {self.title}'

class Certification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    title_awarded_by = models.CharField(max_length=255)
    year_awarded = models.DateField()
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f'Name: {self.user.username}, title : {self.title}'

class SkillSet(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = RichTextField()
    def __str__(self):
        return self.user.username
    
class Project(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_details = RichTextField()
    programming_language = models.CharField(max_length=255)
    def __str__(self):
        return f'Name: {self.user.username}, projects : {self.details}, language : {self.programming_language}'
    
    
    
    
   