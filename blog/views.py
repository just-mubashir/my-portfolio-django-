from operator import imod
from django.shortcuts import render

# Create your views here.
from blog.models import Blog
from blog.forms import BlogForm

def index(request):
    allposts = Blog.objects.all()
    return render (request, 'blog/index.html', {'allposts':allposts} )
def blodpost(request, slug):
    return render (request, 'blog/blogpost.html' )