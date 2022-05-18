from django.forms import ModelForm, TextInput
from blog.models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'